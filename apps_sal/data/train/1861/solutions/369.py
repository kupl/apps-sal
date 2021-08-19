class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # for every pair of points, check if other diagonal is in points
        pointset = set([tuple(x) for x in points])
        res = 2 ** 32
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:  # check points aren't on the same line
                    if (p1[0], p2[1]) in pointset and (p2[0], p1[1]) in pointset:  # check other diag is in points
                        res = min(res, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))  # update res
        return res if res < 2 ** 32 else 0
