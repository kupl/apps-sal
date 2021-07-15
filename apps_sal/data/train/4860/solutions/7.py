from functools import reduce

def amidakuji(ar):
    *ints, = range(1 + len(ar[0]))
    return reduce(swap, ar, ints)

def swap(acc, rungs):
    for r, rung in enumerate(rungs):
        if rung == '1':
            acc[r : r + 2] = acc[r + 1], acc[r]
    return acc
