# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(T, case):
    def solver(X, Y):
        X = (X - X // 3 if X > 0 else X + (2 - X) // 3) - 1
        Y = (Y - Y // 3 if Y > 0 else Y + (2 - Y) // 3) - 1
        if X == Y == 0:
            return 0
        if X == Y == 1:
            return 1
        return max(X, -X, Y, -Y) + (X == Y)

    for ax, ay, bx, by, cx, cy in case:
        print((solver(ax + bx + cx, ay + by + cy)))


def __starting_point():
    T = int(input())
    case = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, case)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()


__starting_point()
