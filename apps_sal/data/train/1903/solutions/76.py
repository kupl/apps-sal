class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        p = [0] * len(points)
        for i in range(len(points)):
            p[i] = i
        pq = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(pq, [dis, i, j])

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            if x > y:
                (x, y) = (y, x)
            p[y] = x
        res = 0
        while len(pq) > 0:
            (dis, i, j) = heapq.heappop(pq)
            if find(i) == find(j):
                continue
            res += dis
            union(find(i), find(j))
        return res
