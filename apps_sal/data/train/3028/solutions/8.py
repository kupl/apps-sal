from functools import reduce
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return reduce((lambda x, y: x*y), range(1, n+1))
