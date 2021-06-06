# example3-16.py
import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('I have finished.')
    
loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(fut.done())
# False

print(loop.create_task(main(fut)))
# <Task pending name='Task-1' coro=<main() running at example3-16.py:4>>

print(loop.run_until_complete(fut))
# I have finished.

print(fut.done())
# True

print(fut.result())
# I have finished.
