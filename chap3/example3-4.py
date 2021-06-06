# Example 3-4
async def f():
    return 123
print(type(f))
# <class 'function'>

import inspect
print(inspect.iscoroutinefunction(f))
# True

def g():
    yield 123

print(type(g))
# <class 'function'>

gen = g()
print(type(gen))
# <class 'generator'>
