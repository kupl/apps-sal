from collections import defaultdict


class Solution(object):
    def minAreaRect(self, points):
        x_points = defaultdict(list)
        for x, y in points:
            x_points[x].append(y)
        min_area = float('inf')
        vert_lines = {}
        sort_by_x = sorted(x_points)
        for x in sort_by_x:
            y_list = x_points[x]
            y_list.sort()
            for i in range(len(y_list)):
                y2 = y_list[i]
                for j in range(i):
                    y1 = y_list[j]
                    if (y1, y2) in vert_lines:
                        x2 = vert_lines[(y1, y2)]
                        min_area = min(min_area, abs(x - x2) * abs(y1 - y2))
                    vert_lines[(y1, y2)] = x
        return min_area if min_area != float('inf') else 0
