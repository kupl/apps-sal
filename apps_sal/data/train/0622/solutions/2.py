# from bisect import bisect_left as bl
# from bisect import bisect_right as br
# import heapq
# import math
from collections import Counter
# from functools import reduce,cmp_to_key
# import sys
# input = sys.stdin.readline

# M = mod = 998244353
# def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in     range(1, int(n**0.5) + 1) if n % i == 0))))
# def inv_mod(n):return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
# def li2():return [i for i in input().rstrip('\n').split(' ')]
# def li3():return [int(i) for i in input().rstrip('\n')]


def dist(a, b): return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


for _ in range(val()):
    n, m, w, h = li()

    s = Counter(st())
    l = []
    for i in range(m):
        l.append(li())

    ans = float('inf')
    # for i in range(m):
    #     for j in range(i + 1,m):
    #         ans = min(ans,dist(l[i],l[j]))
    l.sort(key=lambda x: x[0])
    for j in range(1, 50):
        for i in range(j, m):
            ans = min(ans, dist(l[i - j], l[i]))
    for i in l:
        if s['D'] or s['U'] > 1:
            ans = min(ans, 2 * i[1])
        if s['U'] or s['D'] > 1:
            ans = min(ans, 2 * (h - i[1]))
        if s['L'] or s['R'] > 1:
            ans = min(ans, 2 * i[0])
        if s['R'] or s['L'] > 1:
            ans = min(ans, 2 * (w - i[0]))
    print(ans)
