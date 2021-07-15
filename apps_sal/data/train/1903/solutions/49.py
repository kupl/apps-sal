class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dis = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j: continue
                dis[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        vis = [False] * N
        heap = [(0, 0)]
        res = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if vis[node]: continue
            vis[node] = True
            res += weight
            for i in range(N):
                if vis[i]: continue
                heapq.heappush(heap, (dis[node][i], i))
        return res

