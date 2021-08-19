class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        min_area = 40000 * 40000 + 1
        seen_points = set()
        for (x, y) in points:
            seen_points.add((x, y))
        for (p1_x, p1_y) in points:
            for (p2_x, p2_y) in points:
                if p1_x > p2_x and p1_y > p2_y:
                    if (p1_x, p2_y) in seen_points and (p2_x, p1_y) in seen_points:
                        area = abs(p2_x - p1_x) * abs(p2_y - p1_y)
                        if area > 0:
                            min_area = min(min_area, area)
        if min_area == 40000 * 40000 + 1:
            return 0
        return min_area
