# example3-8.py
coro = f()
coro.send(None)
coro.throw(Exception, 'blah')
