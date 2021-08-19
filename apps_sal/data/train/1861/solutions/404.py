class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Let's make a set of points
        # With two nested loops, find points (x1, y1) and (x2, y2) and use those to see if (x1,y2) and (x2,y1) are in the sets
        points_set = {tuple(p) for p in points}
        res = float('inf')
        for p1 in points:
            for p2 in points:
                # Find diagonal points
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    if area < res:
                        if ((p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set):
                            res = area
        return 0 if res == float('inf') else res
