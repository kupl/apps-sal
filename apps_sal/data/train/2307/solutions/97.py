import bisect
import heapq
import itertools
import sys
import math
import random
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor
from typing import List
mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def main():
    (N, A, B) = lmi()
    X = lmi()
    ans = 0
    for i in range(1, N):
        ans += min((X[i] - X[i - 1]) * A, B)
    print(ans)


def __starting_point():
    main()


__starting_point()
