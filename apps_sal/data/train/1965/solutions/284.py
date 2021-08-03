class UnionFind:
    def __init__(self, n):
        self.parents = list(range(1, n + 1))

    def find(self, x):
        if x != self.parents[x - 1]:
            self.parents[x - 1] = self.find(self.parents[x - 1])
        return self.parents[x - 1]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parents[px - 1] = py


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        Ua = UnionFind(n)
        Ub = UnionFind(n)
        edges = sorted(edges, reverse=True)
        for edge in edges:
            if edge[0] == 3:
                idx = False
                if Ua.find(edge[1]) == Ua.find(edge[2]):
                    out += 1
                    idx = True
                else:
                    Ua.union(edge[1], edge[2])
                if Ub.find(edge[1]) == Ub.find(edge[2]):
                    if not idx:
                        out += 1
                else:
                    Ub.union(edge[1], edge[2])

            elif edge[0] == 2:
                if Ub.find(edge[1]) == Ub.find(edge[2]):
                    out += 1
                else:
                    Ub.union(edge[1], edge[2])

            else:
                if Ua.find(edge[1]) == Ua.find(edge[2]):
                    out += 1
                else:
                    Ua.union(edge[1], edge[2])

        if len(set(Ua.find(i) for i in range(1, n + 1))) != 1 or len(set(Ub.find(i) for i in range(1, n + 1))) != 1:
            return -1
        else:
            return out
