class Solution:

    def numPoints(self, points: List[List[int]], r: int) -> int:
        n = len(points)
        result = 1

        def calc_dist(pt1, pt2):
            (x1, y1) = pt1
            (x2, y2) = pt2
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        def get_centers(i, j):
            d_xy = calc_dist(points[i], points[j])
            if d_xy > r * 2:
                return []
            delta_x = points[j][0] - points[i][0]
            delta_y = points[j][1] - points[i][1]
            x_mid = points[i][0] + delta_x / 2
            y_mid = points[i][1] + delta_y / 2
            if d_xy == r * 2:
                return [(x_mid, y_mid)]
            d = math.sqrt(r ** 2 - (d_xy / 2) ** 2)
            return [(x_mid + d * delta_y / d_xy, y_mid - d * delta_x / d_xy), (x_mid - d * delta_y / d_xy, y_mid + d * delta_x / d_xy)]

        def count_points_inside(center, i, j):
            count = 2
            for idx in range(n):
                if idx == i or idx == j:
                    continue
                count += calc_dist(center, points[idx]) <= r
            return count
        for i in range(n):
            for j in range(i + 1, n):
                centers = get_centers(i, j)
                for center in centers:
                    result = max(result, count_points_inside(center, i, j))
        return result
