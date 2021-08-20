class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        ref = set(map(tuple, points))
        minArea = float('inf')
        curArea = 0
        for (i, p2) in enumerate(points):
            for j in range(i):
                p1 = points[j]
                if (p1[0] != p2[0] and p1[1] != p2[1]) and (p1[0], p2[1]) in ref and ((p2[0], p1[1]) in ref):
                    curArea = abs(p2[0] - p1[0]) * abs(p2[1] - p1[1])
                    minArea = min(minArea, curArea)
        return minArea if minArea != float('inf') else 0
