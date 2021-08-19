import sys
from datetime import datetime as dt
dformat = '%a %d %b %Y %H:%M:%S %z'


def time_delta(t1, t2):
    first = dt.strptime(t1, dformat)
    second = dt.strptime(t2, dformat)
    return int(abs((first - second).total_seconds()))


def __starting_point():
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)


__starting_point()
