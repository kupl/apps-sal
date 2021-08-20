class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = i = connected = 0
        min_d = [10 ** 7] * n
        while connected < n - 1:
            min_d[i] = float('inf')
            min_j = i
            for j in range(n):
                if min_d[j] != float('inf'):
                    min_d[j] = min(min_d[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                    min_j = j if min_d[j] < min_d[min_j] else min_j
            ans += min_d[min_j]
            i = min_j
            connected += 1
        return ans
