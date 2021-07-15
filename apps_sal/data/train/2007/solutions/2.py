import sys
from itertools import *
from math import *
def solve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    ss, ll = 0, int(2.1e10)
    while ss < ll:
        avg = (ss + ll) // 2
        works = True
        hidx = 0
        pidx = 0
        while hidx < len(h) and pidx < len(p):
            leftget = p[pidx]
            curpos = h[hidx]
            if curpos - leftget > avg:
                works = False
                break
            getbacktime = max(0, 2*(curpos - leftget))
            alsotoright = max(0, avg - getbacktime)
            leftime = max(0, curpos - leftget)
            remtime = max(0, (avg - leftime) // 2)
            furthestright = curpos + max(alsotoright, remtime)
            while pidx < len(p) and p[pidx] <= furthestright: pidx += 1
            hidx += 1
        if pidx != len(p): works = False
        if works: ll = avg
        else: ss = avg + 1
    print(ss)


if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()
