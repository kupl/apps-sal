class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        pointSet = set()
        for (x, y) in points:
            pointSet.add((x, y))
        length = len(points)
        minArea = float('inf')
        for i in range(length):
            for j in range(i, length):
                p1 = points[i]
                p2 = points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in pointSet and (p2[0], p1[1]) in pointSet:
                        minArea = min(minArea, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        if minArea == float('inf'):
            return 0
        return minArea
