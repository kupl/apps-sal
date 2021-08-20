class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        lookup = set()
        for (x1, y1) in points:
            for (x2, y2) in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            lookup.add((x1, y1))
        return res if res != float('inf') else 0
