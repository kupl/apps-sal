class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ind = 0
        distance = [float('inf')] * n
        visited = [False] * n
        total_cost = 0
        for cnt in range(n):
            (x0, y0) = (points[ind][0], points[ind][1])
            for i in range(n):
                if visited[i]:
                    continue
                distance[i] = min(distance[i], abs(points[i][0] - x0) + abs(points[i][1] - y0))
            (dis, ind) = min(((d, i) for (i, d) in enumerate(distance)))
            visited[ind] = True
            total_cost += dis
            distance[ind] = float('inf')
        return total_cost
