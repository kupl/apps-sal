class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        hs = set()
        N = len(points)
        res = float('inf')
        for i in range(N):
            (x1, y1) = points[i]
            for (x2, y2) in hs:
                if (x1, y2) in hs and (x2, y1) in hs:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            hs.add((x1, y1))
        return res if res != float('inf') else 0
