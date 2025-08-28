import os
#Typing sirve para definir tipos de datos
import typing as t
#Request sirve para hacer peticiones HTTP
import requests
#utils sirve para importar las funciones del otro archivo
import utils
import aiohttp
import asyncio

async def download_and_save_sprite(pokemon, output_dir):
    """Download and save a single pokemon."""
    # This line was not indented correctly
    async with aiohttp.ClientSession() as session:
        content = await utils.maybe_download_sprite_async(session, pokemon["Sprite"])
        if content is not None:
            target_dir = os.path.join(output_dir, pokemon["Type1"])
            await utils.maybe_create_dir_async(target_dir)
            filepath = os.path.join(target_dir, pokemon["Pokemon"] + ".png")
            await asyncio.to_thread(utils.write_binary, filepath, content)
            
@utils.timeit
async def main(output_dir: str, inputs: t.List[str]):
    """Download for all intpus and place them in output_dir."""
    await utils.maybe_create_dir_async(output_dir)
    all_pokemons = [row async for row in utils.read_pokemons_async(inputs)]
    tasks = [download_and_save_sprite(pokemon, output_dir) for pokemon in all_pokemons]
    await asyncio.gather(*tasks)

    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="directory to store the data")
    parser.add_argument("inputs", nargs="+", help="list of files with metadata")
    args = parser.parse_args()
    utils.maybe_remove_dir(args.output_dir)
    asyncio.run(main(args.output_dir, args.inputs))