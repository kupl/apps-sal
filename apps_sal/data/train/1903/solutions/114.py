class UnionFindGraph(dict):
    def union(self, p: Hashable, q: Hashable):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)
        self[rootOfP] = rootOfQ

    def isConnected(self, p: Hashable, q: Hashable) -> bool:
        return self.root(p) == self.root(q)

    def root(self, r: Hashable) -> Hashable:

        while r != self[r]:
            self[r] = self[self[r]]
            r = self[r]

        return r


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = UnionFindGraph()
        edges = []

        for i, v in enumerate(points):

            for j, w in enumerate(points[i + 1:], i + 1):
                if i != j:
                    edges.append(((tuple(v), tuple(w)), self.distance(v, w)))

        edges.sort(key=lambda v: v[1])
        res = 0

        for (a, b), distance in edges:
            if a not in graph:
                graph[a] = a
            if b not in graph:
                graph[b] = b

            if not graph.isConnected(a, b):
                res += distance
                graph.union(a, b)

        return res

    def distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
