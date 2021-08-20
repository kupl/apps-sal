class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        pointSet = set(map(tuple, points))
        n = len(points)
        minArea = float('inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                (diag1, diag2) = (points[i], points[j])
                if diag2[0] == diag1[0] or diag2[1] == diag1[1]:
                    continue
                if (diag2[0], diag1[1]) not in pointSet:
                    continue
                if (diag1[0], diag2[1]) not in pointSet:
                    continue
                minArea = min(minArea, abs(diag2[0] - diag1[0]) * abs(diag2[1] - diag1[1]))
        return minArea if minArea < float('inf') else 0
