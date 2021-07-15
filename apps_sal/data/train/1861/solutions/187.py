class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        points.sort(key=lambda a: a[0] * 10 ** 6 + a[1])
        min_array = float(\"inf\")
        point_dict = {}
        current_layer = -1
        current_points = []
        for y, x in points:
            if y != current_layer:
                for old_x in current_points:
                    point_dict.setdefault(old_x, set()).add(current_layer)
                current_layer = y
                current_points = []
            if x in point_dict:
                for previous_x in current_points:
                    valid_y = point_dict[x].intersection(point_dict[previous_x])
                    if valid_y:
                        min_array = min(min_array, (y - max(valid_y)) * (x - previous_x))
                current_points.append(x)
            else:
                point_dict.setdefault(x, set()).add(y)
        if min_array == float(\"inf\"):
            return 0
        else:
            return min_array
