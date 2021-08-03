class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p_set = set([(x, y) for x, y in points])

        res = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                up = (p1[0], p2[1])
                left = (p2[0], p1[1])
                if up in p_set and left in p_set:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    res = min(res, area)

        return res if res < float('inf') else 0
