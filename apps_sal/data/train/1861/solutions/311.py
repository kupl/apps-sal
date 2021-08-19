class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        points.sort()
        for point in points:
            point_set.add((point[0], point[1]))

        def getArea(point1: List[int], point2: List[int]) -> int:
            if point2[0] <= point1[0] or point2[1] <= point1[1]:
                return 0
            if (point1[0], point2[1]) in point_set and (point2[0], point1[1]) in point_set:
                return (point2[0] - point1[0]) * (point2[1] - point1[1])
            return 0
        min_area = math.inf
        N = len(points)
        for i in range(N):
            start_point = points[i]
            for j in range(i + 1, N):
                area = getArea(start_point, points[j])
                if area > 0:
                    min_area = min(min_area, area)
        return min_area if min_area != math.inf else 0
