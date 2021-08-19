from collections import deque
from itertools import count, dropwhile


def iter_seq(init):
    ds = deque(map(int, str(init)))
    while True:
        n = sum(ds)
        yield n
        ds.popleft()
        ds.append(n)


def is_keith_number(n):
    if n < 10:
        return False
    (i, d) = next(dropwhile(lambda x: x[1] < n, enumerate(iter_seq(n), 1)))
    return i if d == n else False
