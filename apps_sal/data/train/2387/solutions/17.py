import sys
import math
import bisect
import itertools
import random
import re


def solve(n):
    ans = 0
    while n:
        if n < 10:
            ans += n
            n = 0
        else:
            ans += n // 10 * 10
            n = n // 10 + n % 10
    return ans


def main():
    for _ in range(int(input())):
        n = int(input())
        print(solve(n))


def __starting_point():
    main()


__starting_point()
