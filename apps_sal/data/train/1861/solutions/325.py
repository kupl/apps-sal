class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        points = sorted(points)

        points_set = set([tuple(p) for p in points])

        min_area = 999999999999

        has_rectangle = False

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]

                x2 = points[j][0]
                y2 = points[j][1]

                # check (x1, y2) and (x2, y1)

                if x1 == x2:
                    continue

                if y1 == y2:
                    continue

                if (x1, y2) not in points_set:
                    continue

                if (x2, y1) not in points_set:
                    continue

                area = abs((x1 - x2) * (y1 - y2))

                has_rectangle = True

                if area < min_area:
                    min_area = area

        if not has_rectangle:
            return 0
        else:
            return min_area
