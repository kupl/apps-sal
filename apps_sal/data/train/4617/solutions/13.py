from itertools import count

def f():
    c = count()
    while True: yield 2 ** next(c)

def powers_of_two(n):
    iter = f()
    r = [next(iter) for x in range(n + 1)]
    return r
