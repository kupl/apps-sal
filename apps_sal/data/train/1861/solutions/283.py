class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        pointset = set()
        for (x, y) in points:
            pointset.add((x, y))
        minarea = float('inf')
        for (x1, y1) in pointset:
            for (x2, y2) in pointset:
                if x1 > x2 and y1 > y2 and ((x1, y2) in pointset) and ((x2, y1) in pointset):
                    area = abs(x1 - x2) * abs(y1 - y2)
                    minarea = min(minarea, area)
        if minarea == float('inf'):
            return 0
        else:
            return minarea
