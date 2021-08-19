class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = [False] * len(points)

        def manhattan(x, y):
            return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        d = [[0 for j in range(len(points))] for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                p = manhattan(i, j)
               # print(p)
                d[i][j] = p
                d[j][i] = p

        q = []

        heapq.heappush(q, (0, 0))
        m = {}

        while q:
            dist, j = heapq.heappop(q)
            if j in m:
                continue
            m[j] = dist
          #  print(j,m[j])
            for i in range(len(points)):
                if i not in m:
                    heapq.heappush(q, (d[j][i], i))
        # print(m)
        return sum(m.values()) if len(m) == len(points) else 0
