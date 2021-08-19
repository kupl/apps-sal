#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

# Go from node start and return a list of visited nodes


def dfs(graph, seen, start):
    if seen[start]:
        return None

    visit = [start]
    ans = []
    while visit:
        node = visit.pop()
        seen[node] = True
        ans.append(node)
        for v in graph[node]:
            if not seen[v]:
                visit.append(v)

    return ans


def main(n, arr):
    orig = {}
    for i in range(n):
        val = arr[i]
        orig[val] = i
    _arr = sorted(arr)

    g = defaultdict(list)
    for i in range(n):
        val = _arr[i]
        origpos = orig[val]
        g[origpos].append(i)  # there's a connection between this two positions

    seen = [False] * n
    ans = []
    for i in range(n):  # ensure we visit all nodes
        if not seen[i]:
            ans.append(dfs(g, seen, i))

    print(len(ans))
    for a in ans:
        print(len(a), " ".join(map(lambda x: str(x + 1), a)))  # add 1 for 1 based index


def __starting_point():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split(" ")))
    main(n, arr)


__starting_point()
