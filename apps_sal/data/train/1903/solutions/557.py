class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.prim(points)

    def generategraph(self, points):
        adjList = defaultdict(list)
        for p in points:
            for q in points:
                if p == q:
                    continue
                adjList[p[0], p[1]].append((abs(p[0] - q[0]) + abs(p[1] - q[1]), (q[0], q[1])))
        return adjList

    def prim(self, points):
        if len(points) <= 1:
            return 0
        adjList = self.generategraph(points)
        visited = set()
        minCost = 0
        heap = [(0, tuple(points[0]), tuple(points[0]))]
        print(heap)
        while heap and len(visited) < len(points):
            (cost, u, v) = heapq.heappop(heap)
            if v in visited:
                continue
            minCost += cost
            visited.add(v)
            for (costNei, nei) in adjList[v]:
                if nei in visited:
                    continue
                heapq.heappush(heap, (costNei, v, nei))
        return minCost
