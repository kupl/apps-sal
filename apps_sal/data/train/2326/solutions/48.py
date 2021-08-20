from collections import defaultdict, deque
import sys
import heapq
from bisect import bisect_left, bisect_right
import copy
import math


def getN():
    return int(input())


def getNM():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


INF = 10 ** 17
MOD = 10 ** 9 + 7


def mint(lis):
    return list(map(int, lis))


def bifind(arr_sorted, x):
    idx = bisect_left(arr_sorted, x)
    if idx == len(arr_sorted):
        return False
    if arr_sorted[idx] == x:
        return True
    else:
        return False


def getyaku(n):
    ret = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)
    return ret


def find(x, a):
    idx = bisect_left(a, x)
    if idx == len(a):
        return False
    if a[idx] == x:
        return True
    else:
        return False


def main():
    n = getN()
    nums = getList()
    nums = [(x, i + 1) for (i, x) in enumerate(nums)]
    nums.append((0, INF))
    nums.sort(key=lambda x: -x[0] * INF + x[1])
    mx = INF
    ans = [0 for i in range(n + 1)]
    tmp_tgt = INF
    through = 0
    for (a, b) in nums:
        if a != mx:
            diff = mx - a
            if mx != INF:
                ans[tmp_tgt] += through * diff
            mx = a
            if b < tmp_tgt:
                tmp_tgt = b
        through += 1
    for an in ans[1:]:
        print(an)


def __starting_point():
    main()


__starting_point()
