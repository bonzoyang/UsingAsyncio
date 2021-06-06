# example3-12.py
import asyncio
loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop is loop2)
