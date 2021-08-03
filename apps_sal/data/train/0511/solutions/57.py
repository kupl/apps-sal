# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, As):
    all_xor = 0
    for A in As:
        all_xor ^= A
    ans = ''
    for A in As:
        ans += str(A ^ all_xor) + ' '
    print((ans[:-1]))


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)


__starting_point()
