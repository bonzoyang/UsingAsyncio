# example3-13.py
import asyncio
async def g():
    print(123)
    return 123

async def f():
    await asyncio.sleep(2.0)
    # create take
    
    loop = asyncio.get_event_loop()
    for i in range(2):
        coro = g()
        loop.create_task(coro)

    
loop = asyncio.get_event_loop()
coro = f()
loop.run_until_complete(coro)
