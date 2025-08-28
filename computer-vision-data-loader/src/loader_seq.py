import dataclasses
import pathlib
import requests
import time
import matplotlib.pyplot as plt
from typing import Annotated, Callable, Iterator, Sequence

import numpy as np
from numpy.typing import NDArray
import csv
from PIL import Image
from io import BytesIO
import math


@dataclasses.dataclass
class Row:
    image: NDArray[np.uint8]
    name: str


def download(source: str) -> bytes:
    response = requests.get(source)
    return response.content


def load(
    sources: Sequence[Annotated[pathlib.Path, "CSV File"]],
    *,
    downloader: Callable[[str], bytes] = download,
) -> Iterator[Row]:
    for source in sources:
        with source.open("r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["Pokemon"]
                url = row["Sprite"]
                image_data = downloader(url)
                image = Image.open(BytesIO(image_data)).convert("RGB")
                image_array = np.asarray(image, dtype=np.uint8)
                yield Row(image=image_array, name=name)
               
if __name__ == "__main__":
    csv_file_path = pathlib.Path("..", "data", "pokemon-gen1-data.csv")
    total_start_time = time.perf_counter()
    all_pokemons = list(load(sources=[csv_file_path]))

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
                
            