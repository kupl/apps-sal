class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))

        if res != float('inf'):
            return res
        else:
            return 0
