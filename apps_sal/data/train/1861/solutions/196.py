class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        x_vals = defaultdict(set)
        y_vals = defaultdict(set)
        for p in points:
            x_vals[p[0]].add(p[1])
            y_vals[p[1]].add(p[0])
        min_area = 40000 * 40000 + 1
        for (x, y_coords) in list(x_vals.items()):
            if len(y_coords) == 1:
                continue
            y_list = list(y_coords)
            for (i, y_1) in enumerate(y_list):
                for (j, y_2) in enumerate(y_list[i + 1:]):
                    common_x_2 = y_vals[y_1].intersection(y_vals[y_2])
                    common_x_2.remove(x)
                    for x_2 in list(common_x_2):
                        min_area = min(min_area, abs(x_2 - x) * abs(y_2 - y_1))
        if min_area == 40000 * 40000 + 1:
            return 0
        return min_area
