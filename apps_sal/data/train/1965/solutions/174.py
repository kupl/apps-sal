import copy
from collections import defaultdict


class DSU:

    def __init__(self, reps):
        self.reps = reps

    def find(self, x):
        if not x == self.reps[x]:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]

    def union(self, x, y):
        self.reps[self.find(y)] = self.find(x)


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        es = [[], [], [], []]
        for (i, u, v) in edges:
            es[i].append((u, v))
        dsu = DSU(reps={x: x for x in range(1, n + 1)})
        for (u, v) in es[3]:
            dsu.union(u, v)
        islands = defaultdict(set)
        for x in range(1, n + 1):
            islands[dsu.find(x)].add(x)
        if len(islands) == 1:
            return len(es[3]) - (n - 1) + len(es[1]) + len(es[2])
        dA = copy.deepcopy(dsu)
        for (u, v) in es[1]:
            dA.union(u, v)
        islandsA = defaultdict(set)
        for x in range(1, n + 1):
            islandsA[dA.find(x)].add(x)
        if len(islandsA) > 1:
            return -1
        dB = copy.deepcopy(dsu)
        for (u, v) in es[2]:
            dB.union(u, v)
        islandsB = defaultdict(set)
        for x in range(1, n + 1):
            islandsB[dB.find(x)].add(x)
        if len(islandsB) > 1:
            return -1
        return len(edges) - (n - len(islands)) - (len(islands) - 1) * 2
