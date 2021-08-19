class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(i, j):
            (p1, p2) = (points[i], points[j])
            res = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            return res
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    graph[i].append((dist(i, j), j))
        visited = set([])
        root = 0
        visited.add(root)
        edges = [pair for pair in graph[root]]
        res = 0
        heapq.heapify(edges)
        while edges:
            (cost, nex) = heapq.heappop(edges)
            if nex not in visited:
                res += cost
                visited.add(nex)
                for pair in graph[nex]:
                    if pair[1] not in visited:
                        heapq.heappush(edges, pair)
        return res
