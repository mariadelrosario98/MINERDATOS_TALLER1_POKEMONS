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

if __name__ == "__main__":
    csv_file_path = pathlib.Path("..", "data", "pokemon-gen1-data.csv")
    total_start_time = time.perf_counter()
    
    all_pokemons = load(sources=[csv_file_path])

    total_end_time = time.perf_counter()
    total_time = total_end_time - total_start_time
    print(f"Total time to load all Pokemons: {total_time:.2f} seconds")

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
                
            