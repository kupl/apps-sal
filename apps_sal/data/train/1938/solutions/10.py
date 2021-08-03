class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rects = []
        for x1, y1, x2, y2 in rectangles:
            self.helper(rects, 0, x1, y1, x2, y2)

        ans = 0
        mod = pow(10, 9) + 7
        for x1, y1, x2, y2 in rects:
            ans += ((x2 - x1) * (y2 - y1)) % mod
        return ans % mod

    def helper(self, rects, index, x1, y1, x2, y2):
        if index == len(rects):
            rects.append([x1, y1, x2, y2])
            return

        i1, j1, i2, j2 = rects[index]
        if i1 >= x2 or i2 <= x1 or j1 >= y2 or j2 <= y1:
            self.helper(rects, index + 1, x1, y1, x2, y2)
            return

        if x1 < i1:
            self.helper(rects, index + 1, x1, y1, min(i1, x2), y2)

        if x2 > i2:
            self.helper(rects, index + 1, max(i2, x1), y1, x2, y2)

        if y1 < j1:
            self.helper(rects, index + 1, max(x1, i1), y1, min(x2, i2), j1)

        if y2 > j2:
            self.helper(rects, index + 1, max(x1, i1), j2, min(x2, i2), y2)
