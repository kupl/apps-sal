class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        appeared = set()
        res = math.inf
        for (x1, y1) in points:
            for (x2, y2) in appeared:
                if (x1, y2) in appeared and (x2, y1) in appeared:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            appeared.add((x1, y1))
        return 0 if res == math.inf else res
