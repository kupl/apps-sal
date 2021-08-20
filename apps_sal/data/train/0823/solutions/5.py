from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
import sys
input = sys.stdin.readline


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


t = ri()
for _ in range(t):
    aa = rl()
    n = len(aa)
    answer = 'No'
    for mask in range(1, 2 ** n):
        sum = 0
        for k in range(n):
            if mask & 1 << k:
                sum += aa[k]
        if sum == 0:
            answer = 'Yes'
            break
    print(answer)
