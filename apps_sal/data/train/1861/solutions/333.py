class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        min_area = 40000**2 + 1
        m = len(points)
        points_table = set()

        for x, y in points:
            points_table.add((x, y))
        for i in range(m):
            for j in range(i + 1, m):
                a = points[i]
                b = points[j]
                if a[0] != b[0] and a[1] != b[1]:
                    if ((a[0], b[1]) in points_table) and ((b[0], a[1]) in points_table):
                        z = abs((b[0] - a[0]) * (b[1] - a[1]))
                        min_area = min(min_area, z)
        if min_area == 40000**2 + 1:
            min_area = 0
        return min_area
