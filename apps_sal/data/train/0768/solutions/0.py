# cook your dish here
# cook your dish here
from collections import defaultdict
from math import log2
import sys

sys.setrecursionlimit(10 ** 7)

inf = float("inf")


def find_height(node):
    nodes[node] = 1
    for i in graph[node]:
        nodes[node] += find_height(i)
    return nodes[node]


def find_sum(node):
    suma = nodes[node]
    maxa = 0
    for i in graph[node]:
        maxa = max(find_sum(i), maxa)
    return maxa + suma


for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    graph = defaultdict(set)
    for i in range(len(l)):

        graph[l[i]].add(i + 2)
    nodes = defaultdict(int)
    find_height(1)
    ans = find_sum(1)
    print(ans)
