import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 12
p = 10 ** 9 + 7


def main():
    (N, M) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    S = sum(A)
    if M < S:
        print(0)
        return
    ans = 1
    div = 1
    for i in range(N + S):
        ans *= M + N - i
        div *= N + S - i
        ans %= p
        div %= p
    print(ans * pow(div, p - 2, p) % p)


def __starting_point():
    main()


__starting_point()
