class Solution:

    def numPoints(self, points: List[List[int]], r: int) -> int:

        def circle_centers(p1, p2):
            ([x1, y1], [x2, y2]) = (p1, p2)
            half_dist_2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) / 4
            offset2 = r ** 2 - half_dist_2
            (midx, midy) = ((x1 + x2) / 2, (y1 + y2) / 2)
            if abs(offset2) < 0.0001:
                return [[midx, midy]]
            if offset2 < 0:
                return []
            offset = offset2 ** 0.5
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            (dx, dy) = (offset * (y1 - y2) / dist, offset * (x2 - x1) / dist)
            return [[midx + dx, midy + dy], [midx - dx, midy - dy]]

        def count_members_around(cx, cy):
            print(cx, cy)
            return len([0 for (px, py) in points if (px - cx) ** 2 + (py - cy) ** 2 < r ** 2 + 0.0001])
        result = [count_members_around(cx, cy) for i in range(len(points)) for j in range(i + 1, len(points)) for (cx, cy) in circle_centers(points[i], points[j])]
        if len(result) == 0:
            return 1
        print(result)
        return max(result)
