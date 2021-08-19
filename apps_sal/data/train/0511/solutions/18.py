#!/usr/bin/env python3
import sys
from itertools import chain

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(N: int, A: "List[int]"):
    total = 0
    for a in A:
        total ^= a
    return [total ^ a for a in A]


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, a = map(int, line.split())
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    ans = solve(N, A)
    print((" ".join([str(a) for a in ans])))


def __starting_point():
    main()


__starting_point()
