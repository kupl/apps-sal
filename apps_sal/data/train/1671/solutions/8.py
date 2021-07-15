import io
import os

from collections import Counter, defaultdict, deque


def solve(N,):
    arr = [1] * N
    return " ".join(map(str, arr))


def __starting_point():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    TC = int(input())
    for tc in range(1, TC + 1):
        (N,) = [int(x) for x in input().split()]
        ans = solve(N,)
        print(ans)

__starting_point()
