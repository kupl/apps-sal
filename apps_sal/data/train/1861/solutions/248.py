class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        area = 0
        for (i1, j1) in points:
            for (i2, j2) in points:
                if i1 != i2 and j1 != j2:
                    if (i1, j2) in point_set and (i2, j1) in point_set:
                        if area == 0:
                            area = abs(i1 - i2) * abs(j1 - j2)
                        else:
                            area = min(area, abs(i1 - i2) * abs(j1 - j2))
            point_set.add((i1, j1))
        return area
