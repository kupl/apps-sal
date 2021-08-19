import sys
import math
import bisect


def main():
    for _ in range(int(input())):
        (n, m) = list(map(int, input().split()))
        val = (n + m - 1) * 1.0
        print('%.6f' % val)


def __starting_point():
    main()


__starting_point()
