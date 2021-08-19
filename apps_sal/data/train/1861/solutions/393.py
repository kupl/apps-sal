class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        x_axes = {}
        y_axes = {}
        for point in points:
            if point[0] not in x_axes:
                x_axes[point[0]] = set()
            if point[1] not in y_axes:
                y_axes[point[1]] = set()
            x_axes[point[0]].add(point[1])
            y_axes[point[1]].add(point[0])

        def findMinArea(point, x_axes, y_axes):
            possible_x = y_axes[point[1]]
            possible_y = x_axes[point[0]]
            min_area = None
            for x in possible_x:
                if x == point[0]:
                    continue
                for y in possible_y:
                    if y == point[1]:
                        continue
                    if x in y_axes[y]:
                        area = abs((x - point[0]) * (y - point[1]))
                        min_area = area if min_area is None else min(area, min_area)
            return min_area
        min_area = None
        for point in points:
            area = findMinArea(point, x_axes, y_axes)
            if area is not None:
                min_area = area if min_area is None else min(min_area, area)
        return min_area if min_area else 0
