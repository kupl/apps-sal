#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    import psyco
    psyco.full()
except ImportError:
    pass


def main(n):
    sol = -1

    while (n >= 7 and sol < 0):
        if not (n % 7):
            sol = n
        n -= 4

    return sol


def __starting_point():
    T = int(input())

    for test in range(T):
        N = list(map(int, input().split()))[0]
        print(main(N))


__starting_point()
