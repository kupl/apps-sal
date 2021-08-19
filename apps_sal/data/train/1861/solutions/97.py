class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(((x, y) for (x, y) in points))
        min_rec = math.inf
        for (x1, y1) in points:
            for (x2, y2) in points:
                if x1 < x2 and y1 > y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        min_rec = min(min_rec, (x2 - x1) * (y1 - y2))
        return 0 if min_rec == math.inf else min_rec
