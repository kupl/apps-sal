class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = 999999999999999999
        points = [(l[0], l[1]) for l in points]
        s_points = set(points)
        for p1 in points:
            for p2 in points:
                (x1, y1) = p1
                (x2, y2) = p2
                if x1 == x2 or y1 == y2:
                    continue
                area = abs(x2 - x1) * abs(y2 - y1)
                if area < min_area:
                    if (x1, y2) in s_points and (x2, y1) in s_points:
                        min_area = area
        if min_area is 999999999999999999:
            return 0
        return min_area
