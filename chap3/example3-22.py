# example3-22.py
from contexlib import asynccontextmanager

@asynccontextmanager
async def web_page(url):
    data = await download_webpage(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)
