import dataclasses
import pathlib
import requests
import time
import matplotlib.pyplot as plt
from typing import Annotated, Callable, Iterator, Sequence
import aiohttp
import asyncio
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


async def download(session: aiohttp.ClientSession, source: str) -> bytes:
 async with session.get(source) as response:
    return await response.content.read()


async def load(
    sources: Sequence[Annotated[pathlib.Path, "CSV File"]],
) -> Iterator[Row]:
    all_rows = []
    for source in sources:
        with source.open("r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                all_rows.append(row)
    async with aiohttp.ClientSession() as session:
        task = {
            asyncio.ensure_future(download(session, row["Sprite"])): row 
            for row in all_rows
        }
        downloaded_images_data = await asyncio.gather(*task.keys(), return_exceptions=True)
        pokemon_rows = []

        for i, image_data in enumerate(downloaded_images_data):
            row_data = all_rows[i]
            image = Image.open(BytesIO(image_data)).convert("RGB")
            image_array = np.asarray(image, dtype=np.uint8)
            pokemon_rows.append(Row(image=image_array, name=row_data["Pokemon"]))
            
    return pokemon_rows

if __name__ == "__main__":
    csv_file_path = pathlib.Path("..", "data", "pokemon-gen1-data.csv")
    total_start_time = time.perf_counter()
    all_pokemons = asyncio.run(load(sources=[csv_file_path]))

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
                
            