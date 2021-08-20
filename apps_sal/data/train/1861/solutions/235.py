from itertools import combinations


class Solution:

    def minAreaRect(self, points) -> int:
        point_x = {}
        point_y = {}
        result = float('inf')
        for i in points:
            if point_x.get(i[0]):
                point_x[i[0]].add(i[1])
            else:
                point_x[i[0]] = set([i[1]])
            if point_y.get(i[1]):
                point_y[i[1]].add(i[0])
            else:
                point_y[i[1]] = set([i[0]])
        for i in point_x:
            if len(point_x[i]) < 2:
                continue
            for (y1, y2) in combinations(point_x[i], 2):
                inter = sorted(point_y[y1].intersection(point_y[y2]))
                if len(inter) >= 2:
                    result = min(min([inter[j] - inter[j - 1] for j in range(1, len(inter))]) * abs(y1 - y2), result)
        if result == float('inf'):
            result = 0
        return result
