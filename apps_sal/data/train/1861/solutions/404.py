class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = {tuple(p) for p in points}
        res = float('inf')
        for p1 in points:
            for p2 in points:
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    if area < res:
                        if (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                            res = area
        return 0 if res == float('inf') else res
