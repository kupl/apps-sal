class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = heights[:]
        for e in range(len(hs) - 1, 0, -1):
            mx, ix = float('-inf'), -1
            for i, h in enumerate(hs[:e + 1]):
                if h >= mx:
                    ix, mx = i, h
            hs[e], hs[ix] = hs[ix], hs[e]
        return sum(a != b for a, b in zip(hs, heights))
