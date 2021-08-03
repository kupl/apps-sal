class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hq = []
        in_mst = [False] * len(points)

        def d(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def add_to_hq(i: int):
            for j in range(len(points)):
                if i != j and not in_mst[j]:
                    heapq.heappush(hq, (d(i, j), j))

        heapq.heappush(hq, (0, 0))
        res = 0
        while hq:
            dist, i = heapq.heappop(hq)
            if not in_mst[i]:
                in_mst[i] = True
                res += dist
                add_to_hq(i)

        return res
