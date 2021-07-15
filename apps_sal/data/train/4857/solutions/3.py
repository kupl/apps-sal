from itertools import chain, repeat

def square_up(n):
    return list(chain.from_iterable(
        chain(repeat(0, n-i), range(i, 0, -1))
        for i in range(1, n+1)
    ))
