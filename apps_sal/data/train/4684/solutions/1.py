from itertools import groupby
from operator import not_

def is_hollow(a):
    b = [(x, [*y]) for x, y in groupby(a, key=not_)]
    return len(b) == 1 and b[0][0] and len(b[0][1]) > 2 or len(b) == 3 and [x for x, _ in b] == [0, 1, 0] and len(b[1][1]) > 2 and len(b[0][1]) == len(b[2][1])
