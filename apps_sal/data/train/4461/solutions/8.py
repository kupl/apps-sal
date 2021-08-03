from itertools import tee, chain, starmap
from operator import lt

# found at https://docs.python.org/3.6/library/itertools.html


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def boxes_packing(length, width, height):
    boxes = map(sorted, sorted(zip(length, width, height), key=lambda b: b[0] * b[1] * b[2]))
    return all(starmap(lt, chain.from_iterable(zip(*a) for a in pairwise(boxes))))
