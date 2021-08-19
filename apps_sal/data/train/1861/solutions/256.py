class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for point in points:
            (x, y) = (point[0], point[1])
            for (_x, _y) in seen:
                if (x, _y) in seen and (_x, y) in seen:
                    res = min(res, abs(x - _x) * abs(y - _y))
            seen.add((x, y))
        if res == float('inf'):
            return 0
        return res
