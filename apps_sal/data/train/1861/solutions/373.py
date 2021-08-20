class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        x = 0
        y = 1
        points_set = set()
        for point in points:
            points_set.add((point[x], point[y]))
        if len(points_set) < 4:
            return 0
        best = None
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if p1[x] == p2[x] or p1[y] == p2[y]:
                    continue
                if (p1[x], p2[y]) in points_set and (p2[x], p1[y]) in points_set:
                    area = abs(p2[x] - p1[x]) * abs(p2[y] - p1[y])
                    best = area if best is None else min(best, area)
        return 0 if not best else best
