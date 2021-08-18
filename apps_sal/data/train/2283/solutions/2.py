import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(grid, n, a, b, x, y):
    grid = [(u - 1, v - 1) for u, v in grid]
    a, b = a - 1, b - 1
    console("----- solving ------")

    if 2 * x >= y:
        console("cannot escape evenutally")
        return "Alice"

    d = defaultdict(list)

    for u, v in grid:
        d[u].append(v)
        d[v].append(u)

    visited = [-1 for _ in range(n)]
    visited[a] = 0
    stack = [(a, 0)]

    while stack:
        cur, dist = stack.pop()
        for nex in d[cur]:
            if visited[nex] != -1:
                continue
            visited[nex] = dist + 1
            stack.append((nex, dist + 1))

    console(visited)
    if visited[b] <= x:
        console("catch at first step")
        return "Alice"

    end = visited.index(max(visited))

    visited = [-1 for _ in range(n)]
    visited[end] = 0
    stack = [(end, 0)]

    while stack:
        cur, dist = stack.pop()
        for nex in d[cur]:
            if visited[nex] != -1:
                continue
            visited[nex] = dist + 1
            stack.append((nex, dist + 1))

    console(visited)
    if max(visited) > 2 * x:
        console("big enough")
        return "Bob"

    console("not big enough")
    return "Alice"


def console(*args):
    return


inp = sys.stdin.readlines()
currow = 0
for case_num in range(int(inp[currow])):

    currow = currow + 1
    nrows, a, b, x, y = list(map(int, inp[currow].split()))

    grid = []
    for _ in range(nrows - 1):
        currow = currow + 1
        grid.append(list(map(int, inp[currow].split())))

    res = solve(grid, nrows, a, b, x, y)

    print(res)
