# example3-14.py
import asyncio
async def g():
    print(123)
    return 123

async def f():
    await asyncio.sleep(2.0)
    # create take
    
    for i in range(2):
        coro = g()
        asyncio.create_task(coro)


loop = asyncio.get_event_loop()
coro = f()
loop.run_until_complete(coro)
