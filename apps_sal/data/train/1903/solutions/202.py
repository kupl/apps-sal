class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = [[0 for _ in range(len(points))].copy() for _ in range(len(points))]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[j][i] = graph[i][j]

        costs = 0
        keys = [sys.maxsize] * len(points)
        parent = [0] * len(points)
        visited = parent.copy()
        keys[0] = 0

        def minkey():
            ind = -1
            m = sys.maxsize
            for i in range(len(points)):
                if visited[i] == 0 and keys[i] < m:
                    m = keys[i]
                    ind = i
            return ind

        for _ in range(len(points)):
            x = minkey()
            visited[x] = 1
            for i in range(len(points)):
                if graph[x][i] > 0 and visited[i] == 0 and keys[i] > graph[x][i]:
                    keys[i] = graph[x][i]
                    parent[i] = x

        for i in range(len(points)):
            costs += graph[i][parent[i]]

        return costs
