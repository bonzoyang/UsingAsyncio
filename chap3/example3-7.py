# example3-7.py
import asyncio

async def f():
    await asyncio.sleep(1.0)
    return 123

async def main():
    retult = await f()
    return result

coro = f()
coro.send(None)
coro.throw(Exception, 'blah')
