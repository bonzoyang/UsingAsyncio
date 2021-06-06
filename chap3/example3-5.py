# example3-5.py
async def f():
    return 123

coro = f()
print(type(coro))
# <class 'coroutine'>

import inspect
print(inspect.iscoroutine(coro))
# True
