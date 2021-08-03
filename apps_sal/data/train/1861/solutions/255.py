class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        data = set()
        res = 2 ** 31 - 1

        for x1, y1 in points:
            for x2, y2 in data:
                if (x1, y2) in data and (x2, y1) in data:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            data.add((x1, y1))
        return res if res < 2 ** 31 - 1 else 0
