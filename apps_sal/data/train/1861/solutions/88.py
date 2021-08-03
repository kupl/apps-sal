class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = inf = float('inf')
        seen = set()
        n = len(points)
        for x1, y1 in set(map(tuple, points)):
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    res = min(res, abs((x2 - x1) * (y2 - y1)))
            seen.add((x1, y1))
        return res if res != inf else 0
