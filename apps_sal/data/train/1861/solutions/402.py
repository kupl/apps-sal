class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0

        area = float('inf')
        corners = set([tuple(x) for x in points])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                    if (points[i][0], points[j][1]) in corners and (points[j][0], points[i][1]) in corners:
                        l, w = abs(points[i][0] - points[j][0]), abs(points[i][1] - points[j][1])
                        area = min(area, l * w)
                    # corners.add(tuple(points[i]))
                    # corners.add(tuple(points[j]))

        return 0 if area == float('inf') else area
