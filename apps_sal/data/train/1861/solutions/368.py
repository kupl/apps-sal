class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set([tuple(v) for v in points])
        min_area = None
        for (i, x1y1) in enumerate(points):
            for x2y2 in points[i:]:
                if x1y1[0] == x2y2[0] or x1y1[1] == x2y2[1]:
                    continue
                x1y2 = tuple([x1y1[0], x2y2[1]])
                x2y1 = tuple([x2y2[0], x1y1[1]])
                if x1y2 in points_set and x2y1 in points_set:
                    area = abs((x1y1[0] - x2y2[0]) * (x1y1[1] - x2y2[1]))
                    if min_area is None or area < min_area:
                        min_area = area
        return min_area if min_area else 0
