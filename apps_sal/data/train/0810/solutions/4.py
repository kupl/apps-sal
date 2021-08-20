from collections import defaultdict
import sys
import math as mt
import random
sys.setrecursionlimit(10 ** 6)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


for _ in range(int(input())):
    (n, q) = get_ints()
    hts = get_array()
    for _ in range(q):
        l = get_array()
        if l[0] == 0:
            hts[l[1]] = l[2]
        else:
            ans = -1
            visited = defaultdict(bool)
            for i in range(l[1] + 1):
                visited[hts[i]] = True
            for i in range(l[1] + 1, n):
                if hts[i] > hts[l[1]] and (not visited[hts[i]]):
                    ans = hts[i]
                    break
            print(ans)
