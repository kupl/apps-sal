class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        dist = [0] * n

        def distance(px, py):
            return abs(px[0] - py[0]) + abs(px[1] - py[1])
        for i in range(1, n):
            dist[i] = distance(points[0], points[i])
        flag = [0] * n
        flag[0] = 1
        for i in range(1, n):
            mi = math.inf
            index = -1
            for j in range(1, n):
                if flag[j]:
                    continue
                if mi > dist[j]:
                    index = j
                    mi = dist[j]
            flag[index] = 1
            res += mi
            for j in range(1, n):
                if flag[j]:
                    continue
                dist[j] = min(dist[j], distance(points[j], points[index]))
        return res
