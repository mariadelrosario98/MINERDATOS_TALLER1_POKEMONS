import dataclasses
import pathlib
import requests
import time
import matplotlib.pyplot as plt
from typing import Annotated, Callable, Iterator, Sequence
from concurrent.futures import ProcessPoolExecutor, as_completed
import math
import numpy as np

from numpy.typing import NDArray
import csv
from PIL import Image
from io import BytesIO
import psutil
import threading


@dataclasses.dataclass
class Row:
    image: NDArray[np.uint8]
    name: str


def download(row_data) -> bytes:
    response = requests.get(row_data["Sprite"])
    image_data = response.content
    image = Image.open(BytesIO(image_data)).convert("RGB")
    image_array = np.asarray(image, dtype=np.uint8)
    return Row(image=image_array, name=row_data["Pokemon"])

def load(
    sources: Sequence[Annotated[pathlib.Path, "CSV File"]],
) -> Iterator[Row]:
    all_rows = []
    for source in sources:
        with source.open("r", encoding = "utf-8") as file:
            reader = csv.DictReader(file)
            all_rows.extend(list(reader))

    pokemon_rows = []
    with ProcessPoolExecutor(max_workers= 8) as executor:
        futures = [executor.submit(download, row) for row in all_rows]
        for future in as_completed(futures):
            result = future.result()
            if result:
                pokemon_rows.append(result)
    return pokemon_rows

def medir_recursos(func: Callable):
    """Decorator that measures CPU and memory (RSS) usage of a function."""
    def wrapper(*args, **kwargs):
        proc = psutil.Process()
        
        # Start a thread to sample memory usage for peak RSS
        stop_event = threading.Event()
        peak_rss = {"mb": proc.memory_info().rss / (1024 * 1024)}

        def _mem_sampler():
            while not stop_event.is_set():
                try:
                    rss_mb = proc.memory_info().rss / (1024 * 1024)
                    if rss_mb > peak_rss["mb"]:
                        peak_rss["mb"] = rss_mb
                except psutil.NoSuchProcess:
                    # Process may have terminated, stop sampling
                    break
                time.sleep(0.05)  # Sample every 50 ms

        mem_thread = threading.Thread(target=_mem_sampler, daemon=True)
        mem_thread.start()

        # Measure CPU time and wall time
        start_wall = time.perf_counter()
        ct = proc.cpu_times()
        start_cpu = (ct.user + ct.system)

        try:
            result = func(*args, **kwargs)
        finally:
            stop_event.set()
            mem_thread.join()

        end_wall = time.perf_counter()
        ct2 = proc.cpu_times()
        end_cpu = (ct2.user + ct2.system)

        wall_time = max(end_wall - start_wall, 1e-9)
        cpu_time = max(end_cpu - start_cpu, 0.0)

        # Calculate CPU usage percentage relative to a single CPU
        cpu_percent_1cpu = (cpu_time / wall_time) * 100.0
        return result, cpu_percent_1cpu, peak_rss["mb"]
    return wrapper


@medir_recursos
def decorated_load(sources: Sequence[Annotated[pathlib.Path, "CSV File"]]):
    return load(sources)

if __name__ == "__main__":
    csv_file_path = pathlib.Path("..", "data", "pokemon-gen1-data.csv")
    total_start_time = time.perf_counter()
    
    all_pokemons, cpu_pct_1cpu, peak_rss_mb = decorated_load(sources=[csv_file_path])

    total_end_time = time.perf_counter()
    total_time = total_end_time - total_start_time
    print(f"Total time to load all Pokemons: {total_time:.2f} s")
    print(f"Uso de CPU (por 1 CPU): {cpu_pct_1cpu:.2f}%")
    # Si quieres % sobre todos los núcleos:
    cpu_all = cpu_pct_1cpu / max(psutil.cpu_count(logical=True), 1)
    print(f"Uso de CPU (sobre todos los núcleos): {cpu_all:.2f}%")
    print(f"Pico de RAM (RSS): {peak_rss_mb:.2f} MB")

    num_pokemons = len(all_pokemons)
    grid_size= math.ceil(math.sqrt(num_pokemons))
    fig, axes = plt.subplots(grid_size, grid_size, figsize=(20, 20))
    axes = axes.flatten()

    for i, pokemon_row in enumerate(all_pokemons):
        axes[i].imshow(pokemon_row.image)
        axes[i].set_title(pokemon_row.name, fontsize=8)
        axes[i].axis('off')

    for j in range(num_pokemons, len(axes)):
        axes[j].axis('off')
        
    plt.show()    
                
            