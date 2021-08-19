class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (xp, yp) = (self.find(x), self.find(y))
        if xp == yp:
            return False
        if self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp
            self.rank[yp] += 1
        self.size -= 1
        return True

    def getSize(self):
        return self.size


class Solution:
    import heapq

    def minCostConnectPoints1(self, points: List[List[int]]) -> int:

        def getDist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        (heap, n, visited, res) = ([], len(points), set([0]), 0)
        for i in range(1, n):
            heapq.heappush(heap, (getDist(0, i), (0, i)))
        while len(visited) < n:
            (dist, (i, j)) = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                res += dist
                for k in range(n):
                    if k not in visited:
                        heapq.heappush(heap, (getDist(j, k), (j, k)))
        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        graph.sort(key=lambda x: x[2])
        dsu = DSU(len(points) + 1)
        res = 0
        for (i, j, cost) in graph:
            if dsu.union(i, j):
                res += cost
        return res
