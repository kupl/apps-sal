class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        m = 0
        q = [(0, 0, 0)]
        visited = [0] * n
        dis = [10 ** 9] * n
        dis[0] = 0
        while m < n:
            w, j, i = heapq.heappop(q)
            if visited[i]:
                continue
            visited[i] = 1
            for j in range(n):
                if j == i or visited[j]:
                    continue
                ww = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if ww < dis[j]:
                    dis[j] = ww
                    heapq.heappush(q, (ww, i, j))
            m += 1
            result += w
        return result
