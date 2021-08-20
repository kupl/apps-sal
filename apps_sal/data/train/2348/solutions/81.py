import sys
import queue
import math
import copy
import itertools
import bisect
import collections
import heapq


def main():

    def LI():
        return [int(x) for x in sys.stdin.readline().split()]

    def _LI():
        return [int(x) - 1 for x in sys.stdin.readline().split()]

    def NI():
        return int(sys.stdin.readline())
    N = NI()
    x = LI()
    L = NI()
    m = N.bit_length()
    f = [[N - 1] * N for _ in range(m)]
    j = 0
    for i in range(N - 1):
        while x[i] + L >= x[j + 1]:
            j += 1
            if j >= N - 1:
                break
        else:
            f[0][i] = j
            continue
        break
    for k in range(1, m):
        for i in range(N):
            f[k][i] = f[k - 1][f[k - 1][i]]
    for _ in range(NI()):
        ans = 0
        (a, b) = _LI()
        if a > b:
            (a, b) = (b, a)
        for k in range(m - 1, -1, -1):
            if f[k][a] < b:
                a = f[k][a]
                ans += 2 ** k
        print(ans + 1)


def __starting_point():
    main()


__starting_point()
