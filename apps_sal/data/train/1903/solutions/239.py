class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        count = 0
        distance = [[0] * len(points) for p in points]
        for i in range(len(points)):
            for j in range(len(points)):
                distance[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        cost = 0
        visited[0] = True
        n = len(points)
        close = [1 << 29] * n
        for i in range(1, n):
            close[i] = distance[0][i]
        for k in range(n - 1):
            minCost = 1 << 29
            v = None
            for i in range(n):
                if not visited[i] and minCost > close[i]:
                    v = i
                    minCost = close[i]
            cost += minCost
            visited[v] = True
            for i in range(n):
                if not visited[i]:
                    close[i] = min(close[i], distance[v][i])
        return cost
