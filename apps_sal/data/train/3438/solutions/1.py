import itertools
from itertools import count

def break_down(text):
    numbers = text.split()
    ns = list(range(1, len(numbers[0])))
    for n in ns:
        for idxs in itertools.combinations(ns, n):
            yield [''.join(numbers[0][i:j]) for i, j in zip((0,) + idxs, idxs + (None,))]
            


def next_higher(start_value,k):
    r = 0
    for n in count(start_value+1):
        desire = n * k
        for a in break_down(str(desire)):
            r += sum([int(b) for b in a])
        if r == n:
            return r
        r = 0


