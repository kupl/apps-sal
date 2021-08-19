class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(u, v):
            return abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
        n = len(points)
        ret = 0
        visited = [False] * n
        visited[0] = True
        closest = [0] * n
        for i in range(1, n):
            closest[i] = dist(0, i)
        for _ in range(n - 1):
            mini = float('inf')
            node = -1
            for i in range(n):
                if not visited[i] and closest[i] < mini:
                    mini = closest[i]
                    node = i
            ret += mini
            visited[node] = True
            for i in range(n):
                if not visited[i]:
                    closest[i] = min(closest[i], dist(i, node))
        return ret
