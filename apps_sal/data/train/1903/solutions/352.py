class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dis = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for i in range(n) for j in range(i + 1, n)]
        heapq.heapify(dis)
        father = list(range(n))

        def getfather(x):
            if father[x] != x:
                father[x] = getfather(father[x])
            return father[x]

        def union(x, y):
            fx = getfather(x)
            fy = getfather(y)
            if fx == fy:
                return False
            father[fx] = fy
            return True
        step = 0
        res = 0
        while dis:
            d, i, j = heapq.heappop(dis)
            if union(i, j):
                res += d
                step += 1
                if step == n - 1:
                    break
        return res
