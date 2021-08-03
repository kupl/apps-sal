class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        res = 0
        seen = set()
        seen.add((points[0][0], points[0][1]))
        minD = []
        for i in range(len(points)):
            if (points[i][0], points[i][1]) not in seen:
                heapq.heappush(minD, (abs(points[i][0] - points[0][0]) +
                                      abs(points[i][1] - points[0][1]),
                                      [points[i][0], points[i][1]]
                                      )
                               )
        while len(seen) < len(points):
            while minD:
                curMinD = heapq.heappop(minD)
                if (curMinD[1][0], curMinD[1][1]) not in seen:
                    break

            res += curMinD[0]
            seen.add((curMinD[1][0], curMinD[1][1]))
            for i in range(len(points)):
                if (points[i][0], points[i][1]) not in seen:
                    heapq.heappush(minD, (abs(points[i][0] - curMinD[1][0]) +
                                          abs(points[i][1] - curMinD[1][1]),
                                          [points[i][0], points[i][1]]
                                          )
                                   )

        return res
