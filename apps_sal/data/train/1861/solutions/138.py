class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_table = set()
        for x,y in points:
            point_table.add((x,y))
        minarea = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1>x2 and y1>y2:
                    if (x1,y2) in point_table and (x2,y1) in point_table:
                        area = abs(x1-x2)*abs(y1-y2)
                        if area:
                            area = min(area, minarea)
                            minarea = area
        return minarea if minarea<float('inf') else 0

