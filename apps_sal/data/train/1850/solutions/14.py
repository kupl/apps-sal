from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        g = Graph()
        for u, v in edges:
            g.connect(u, v)

        children = [0] * N
        cumul = [0] * N

        discovered = set()
        stack = [(0, None)]
        while stack:
            u, parent = stack.pop()
            if u not in discovered:
                discovered.add(u)
                stack.append((u, parent))

                for v in g.adj[u]:
                    if v != parent:
                        stack.append((v, u))

            else:
                discovered.remove(u)
                children[u] = sum(1 + children[v] for v in g.adj[u] if v != parent)
                cumul[u] = children[u] + sum(cumul[v] for v in g.adj[u] if v != parent)

        stack = [(0, None)]
        while stack:
            u, parent = stack.pop()
            if parent is not None:
                cumul[u] = cumul[parent] + N - 2 * (children[u] + 1)

            for v in g.adj[u]:
                if v != parent:
                    stack.append((v, u))

        return cumul


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)

    def connect(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)
