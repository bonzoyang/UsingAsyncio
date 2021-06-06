# example3-28.py
import asyncio

async def f(x):
    await asyncio.sleep(0.1)
    return x+100

async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield f, x
        
async def main():
    results = [await f(x) async for f, x in factory(3)]
    print(f'results = {results}')


asyncio.run(main())
# when in jupyter lab, comment last line and uncomment below lines
# loop = asyncio.get_running_loop()
# task = loop.create_task(main())
