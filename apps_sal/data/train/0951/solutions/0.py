import math
from itertools import permutations as p


def diff(li1, li2):
    li_dif = [i for i in li1 if i not in li2]
    return li_dif


def segments(b):
    """A sequence of (x,y) numeric coordinates pairs """
    poly = [(i[0], i[1]) for i in b]
    return zip(poly, poly[1:] + [poly[0]])


def perimeter(poly):
    """A sequence of (x,y) numeric coordinates pairs """
    return abs(sum((math.hypot(x0 - x1, y0 - y1) for ((x0, y0), (x1, y1)) in segments(poly))))


def av(b):
    return sum([i[3] for i in b])


def val(b):
    return sum([i[2] for i in b])


for _ in range(int(input())):
    b = []
    for _ in range(int(input())):
        b.append(list(map(int, input().split())))
    perm = []
    for i in range(1, len(b)):
        for e in p(b, i):
            perm.append(e)
    perm.sort(key=lambda x: val(x))
    yes = []
    for i in perm:
        if av(i) >= perimeter(diff(b, i)):
            good = val(i)
            yes.append(i)
            break
    print(' '.join([str(b.index(i) + 1) for i in yes[0]]))
    x = round(av(yes[0]) - perimeter(diff(b, yes[0])), 2)
    print(f'{x:.2f}')
