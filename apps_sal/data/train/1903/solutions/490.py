class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = [99999999] * n
        d[0] = 0
        added = set()
        ans = 0

        for i in range(n):
            j_min = -1
            d_min = 99999999
            for j in range(n):
                if j not in added:
                    if d[j] < d_min:
                        j_min = j
                        d_min = d[j]
            added.add(j_min)
            ans += d_min

            for k in range(n):
                if k not in added:
                    if abs(points[k][0] - points[j_min][0]) + abs(points[k][1] - points[j_min][1]) < d[k]:
                        d[k] = abs(points[k][0] - points[j_min][0]) + abs(points[k][1] - points[j_min][1])

        return ans
