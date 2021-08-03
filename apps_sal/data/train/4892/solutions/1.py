from itertools import combinations as com
from collections import defaultdict


def area(points):
    (ax, ay), (bx, by), (cx, cy) = points
    return abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2


def find_biggTriang(listPoints):
    allcom = [[[j[0], j[1]] for j in i] for i in set(com(listPoints, 3))]
    aaa = defaultdict(list)
    count = 0
    for i in allcom:
        ar = area(i)
        if ar != 0:
            count += 1
            aaa[ar].append(i)
    maxarea = max(set(aaa.keys()))
    po = aaa[maxarea]
    if len(po) == 1:
        po = po[0]

    return([len(listPoints), len(allcom), count, po, maxarea])
