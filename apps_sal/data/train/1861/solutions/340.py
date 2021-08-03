class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        all_points = set([(point[0], point[1]) for point in points])
        min_area = float('inf')
        for idx, point1 in enumerate(points):
            for idx, point2 in enumerate(points[idx + 1:], start=idx):
                if point1[0] != point2[0] and point1[1] != point2[1] and (point1[0], point2[1]) in all_points and (point2[0], point1[1]) in all_points:
                    min_area = min(min_area, abs(point1[0] - point2[0]) * abs(point1[1] - point2[1]))
        return min_area if min_area != float('inf') else 0
