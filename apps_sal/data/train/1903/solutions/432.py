class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        (n, graph) = (len(points), collections.defaultdict(dict))
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                graph[i][j] = graph[j][i] = d
        (cnt, ans, visited) = (0, 0, [0] * n)
        heap = [(0, 0)]
        d = [float('inf')] * n
        d[0] = 0
        while heap:
            (cost, node) = heapq.heappop(heap)
            if visited[node]:
                continue
            (visited[node], cnt, ans) = (1, cnt + 1, ans + cost)
            for nex in graph[node]:
                if d[nex] > graph[node][nex]:
                    d[nex] = graph[node][nex]
                    heapq.heappush(heap, (d[nex], nex))
        return ans
