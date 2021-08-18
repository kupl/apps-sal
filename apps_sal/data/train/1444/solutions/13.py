from statistics import median
from collections import defaultdict
import collections
import math
from math import log2, sqrt
import sys
sys.setrecursionlimit(pow(10, 6))
inf = float("inf")
mod = pow(10, 9) + 7


def give(l, n, index, visited):
    if index < 0 or index >= n:
        return 0
    if visited[index] == 1:
        return 0
    visited[index] = 1
    theta = 1
    for i in graph[index]:
        theta += give(l, n, i, visited.copy())

    return theta


for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    visited = defaultdict(int)
    graph = defaultdict(set)
    for i in range(len(l)):
        if l[i] == 1:
            graph[i].add(i - 1)
            graph[i].add(i + 1)
        else:
            graph[i].add(i - 2)
            graph[i].add(i - 1)
            graph[i].add(i + 1)
            graph[i].add(i + 2)
    theta = give(l, n, 0, visited.copy())

    print(theta)
