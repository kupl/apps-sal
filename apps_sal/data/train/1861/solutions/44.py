class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        def compute_table(points, axis=0):
            table = {}
            for point in points:
                key, value = point[axis], point[1 - axis]
                if key in table:
                    table[key].append(value)
                else:
                    table[key] = [value]
            return table

        points.sort()
        x_2_y = compute_table(points, 0)
        y_2_x = compute_table(points, 1)
        min_area = float('inf')
        hashed = set([tuple(point) for point in points])
        for point in points:
            x, y = point
            y_candidates = [_y for _y in x_2_y[x] if _y > y]
            x_candidates = [_x for _x in y_2_x[y] if _x > x]
            for c_y in y_candidates:
                for c_x in x_candidates:
                    if (c_x, c_y) in hashed:
                        min_area = min(min_area, abs(c_y - y) * abs(c_x - x))
        if min_area == float('inf'):
            return 0
        return min_area
