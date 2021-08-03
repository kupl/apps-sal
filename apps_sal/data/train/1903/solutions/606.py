class UnionFind:

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        if p == self.id[p]:
            return p
        return self.find(self.id[p])

    def union(self, p, q):
        idp = self.find(p)
        idq = self.find(q)
        if not self.connected(p, q):
            self.id[idp] = idq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(i, j): return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        graph = collections.defaultdict(list)
        hp = []
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i].append((distance(i, j), j))
        start, cost = 0, 0
        visited = {0}

        for to in graph[0]:
            heapq.heappush(hp, to)

        while len(visited) != n and len(hp):
            dist, to = heapq.heappop(hp)
            if to not in visited:
                visited.add(to)
                cost += dist
                for t in graph[to]:
                    heapq.heappush(hp, t)
        return cost
