class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhadistance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        n = len(points)
        if n == 1:
            return 0
        min_distance = [[0 for j in range(n)] for i in range(n)]
        min_flag = float('inf')
        min_point = -1
        queue = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    min_distance[i][j] = manhadistance(points[i], points[j])
                    if min_distance[i][j] < min_flag:
                        min_flag = min_distance[i][j]
                        min_point = i
        # print(min_distance)
        for j in range(n):
            if j != min_point:
                heappush(queue, (min_distance[min_point][j], min_point, j))
        # print(queue)

        res = 0
        visit = [False] * n
        while queue:
            cur = heappop(queue)
            v, x, y = cur

            if not visit[x] or not visit[y]:
                res += cur[0]
                visit[x] = True
                visit[y] = True
            if sum(visit) == n:
                return res
            for j in range(n):
                if not visit[j]:
                    heappush(queue, (min_distance[y][j], y, j))

        return res
