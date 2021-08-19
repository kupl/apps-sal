#!/usr/bin/env pypy3

import collections


INF = 10 ** 10


def solve(n, t, xs):
    trades = collections.Counter()
    maxs = [INF for _ in range(n)]
    maxs[n - 1] = xs[n - 1]
    for i in range(n - 1)[::-1]:
        maxs[i] = max(xs[i], maxs[i + 1])
    for i in range(n):
        delta = maxs[i] - xs[i]
        if delta > 0:
            trades[delta] += 1
    max_delta = max(trades.keys())
    return trades[max_delta]


def main():
    n, t = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    print((solve(n, t, xs)))


def __starting_point():
    main()


__starting_point()
