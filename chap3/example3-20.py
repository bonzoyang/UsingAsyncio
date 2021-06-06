# example3-20.py
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return conn
    async def __aexit__(self, exec_type, exc, tb):
        await self.conn.close()
        
async with Connection('localhost', 9001) as conn:
    pass
