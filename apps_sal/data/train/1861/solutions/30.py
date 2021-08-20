class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        sorted_points = {}
        for point in points:
            if point[0] not in sorted_points:
                sorted_points[point[0]] = []
            sorted_points[point[0]].append(point)
        sorted_col = sorted(sorted_points.keys())
        min_area = None
        seen = {}
        for col in sorted_col:
            sorted_points[col] = sorted(sorted_points[col])
            for idx1 in range(len(sorted_points[col])):
                for idx2 in range(idx1 + 1, len(sorted_points[col])):
                    point1 = sorted_points[col][idx1]
                    point2 = sorted_points[col][idx2]
                    if (point1[1], point2[1]) in seen:
                        temp = (point2[1] - point1[1]) * (col - seen[point1[1], point2[1]])
                        min_area = min(min_area, temp) if min_area is not None else temp
                    seen[point1[1], point2[1]] = col
        return min_area if min_area is not None else 0
