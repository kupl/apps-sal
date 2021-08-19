def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n, q = map(int, input().split())
    l = []
    for _ in range(n):
        s, t, x = map(int, input().split())
        l.append((s, t, x))
    l.sort(key=lambda a: a[2])
    start = [int(input()) for _ in range(q)]

    skip = [-1] * q
    res = [-1] * q

    for s, t, x in l:
        left = bisect_left(start, s - x)
        right = bisect_left(start, t - x)
        while left < right:
            if skip[left] == -1:
                res[left] = x
                skip[left] = right
                left += 1
            else:
                left = skip[left]

    for i in res:
        print(i)


def __starting_point():
    main()


__starting_point()
