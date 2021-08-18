import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        ques = []
        final = (1 << n) - 1
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(ques, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        p = [i for i in range(n)]
        k = [1 for i in range(n)]
        components = n
        res = 0

        def findp(x):
            while x != p[x]:
                x = p[x]
            return x

        def union(x, y):
            if k[x] > k[y]:
                k[x] += k[y]
                p[y] = x
            else:
                k[y] += k[x]
                p[x] = y

        while components != 1:

            dist, one, two = heapq.heappop(ques)
            pone = findp(one)
            ptwo = findp(two)
            if pone != ptwo:
                union(pone, ptwo)
                components -= 1
                res += dist
        return res
