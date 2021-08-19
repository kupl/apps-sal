class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #         res = 2**31
        #         s = {(p[0], p[1]) for p in points}

        #         for i, p1 in enumerate(points):
        #             for j, p2 in enumerate(points[i + 1:]):
        #                 if p1[0] != p2[0] and p1[1] != p2[1]:
        #                     if (p1[0], p2[1]) in s and (p2[0], p1[1]) in s:
        #                         res = min(res, abs(p1[1] - p2[1]) * abs(p1[0] - p2[0]))
        #         res = res if res < 2**31 else 0
        #         return res

        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0
