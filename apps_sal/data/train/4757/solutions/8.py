import io
import os

from collections import Counter, defaultdict, deque


def solve(R, C, A, B):
    if R * A != C * B:
        return "NO"
    grid = [[0 for c in range(C)] for r in range(R)]
    for r in range(R):
        for i in range(A):
            grid[r][(r * A + i) % C] = 1

    return "YES\n" + "\n".join("".join(map(str, row)) for row in grid)


def __starting_point():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input())
    for t in range(T):
        N, M, A, B = [int(x) for x in input().split()]
        ans = solve(N, M, A, B)
        print(ans)

__starting_point()
