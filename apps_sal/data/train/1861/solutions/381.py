class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        min_area = sys.maxsize

        point_set = set([(p[0], p[1]) for p in points])

        for i in range(len(points)):

            for j in range(i + 1, len(points)):

                p1 = points[i]

                p2 = points[j]

                if p1[0] != p2[0] and p1[1] != p2[1]:

                    p3 = (p1[0], p2[1])

                    p4 = (p2[0], p1[1])

                    if p3 in point_set and p4 in point_set:

                        min_area = min(min_area, abs((p1[0] - p2[0]) * (p1[1] - p2[1])))

        return min_area if min_area != sys.maxsize else 0
