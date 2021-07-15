class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                adj[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[j][i] = adj[i][j]
        selected = [False for _ in range(n)]
        min_edges = [[inf, -1] for _ in range(n)]
        min_edges[0][0] = 0
        total = 0
        for i in range(n):
            v = -1
            for j in range(n):
                if not selected[j] and (v == -1 or min_edges[j][0] < min_edges[v][0]):
                    v = j
            selected[v] = True
            total += min_edges[v][0]
            for to in range(n):
                if adj[v][to] < min_edges[to][0]:
                    min_edges[to][0] = adj[v][to]
        return total
