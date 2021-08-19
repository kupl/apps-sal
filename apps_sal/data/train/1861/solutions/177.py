from itertools import product


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        # create the row and col dicts
        if not points or not points[0]:
            return 0

        m, n = len(points), len(points[0])

        d_row, d_col = {}, {}

        for r, c in points:
            d_row[r] = d_row.get(r, []) + [c]
            d_col[c] = d_col.get(c, []) + [r]

        # while iterating through the list, check if there are:
        # 1. if there's another point in the same col
        # 2. if there's another point in the same row
        # 3. if there's point that can make a rectangle with points from 2, 3
        # only consider points to the down/right

        for r in d_row:
            d_row[r] = sorted(d_row[r])

        for c in d_col:
            d_col[c] = sorted(d_col[c])

        area = float('inf')
        for r, c, in points:
            c2s = [x for x in d_row[r] if x > c]
            r2s = [x for x in d_col[c] if x > r]
            if not c2s or not r2s:
                continue

            for r2, c2 in product(r2s, c2s):
                if c2 in d_row[r2]:
                    area = min(area, (r2 - r) * (c2 - c))

        return area if area < float('inf') else 0
