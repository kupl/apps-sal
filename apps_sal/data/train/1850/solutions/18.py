from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        g = Graph()
        for u, v in edges:
            g.connect(u, v)
            g.connect(v, u)

        t = g.tree(0)

        children = [0] * N
        dists = [0] * N

        discovered = set()
        stack = [0]
        while stack:
            u = stack.pop()
            if u not in discovered:
                discovered.add(u)
                stack.append(u)

                for v in t.adj[u]:
                    stack.append(v)

            else:
                discovered.remove(u)
                children[u] = sum(1 + children[v] for v in t.adj[u])
                dists[u] = children[u] + sum(dists[v] for v in t.adj[u])

        stack = [0]
        while stack:
            u = stack.pop()
            for v in t.adj[u]:
                dists[v] = dists[u] - children[v] - 1 + N - children[v] - 1
                stack.append(v)

        return dists


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)

    def connect(self, u, v):
        self.adj[u].add(v)

    def tree(self, start):
        t = Graph()
        stack = [start]
        while stack:
            u = stack.pop()
            for v in self.adj[u]:
                if v not in t.adj:
                    stack.append(v)
                    t.connect(u, v)

        return t
