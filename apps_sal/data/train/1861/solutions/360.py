'''

    When we see new x point, we establish base point x as baseX.
    For every baseX, there will be multiple y points (y_for_baseX array)
    If y was registered in previous base(for base in y_for_baseX), we update res.
        In other words, we update res if (y, base) seen before at another x.
    We also update x value of seen[base][y]
    After processing, we append y to bases array.
    Return res

'''


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        base_x_to_y = collections.defaultdict(dict)
        y_for_base_x = []
        base_x = -1
        min_area = float('inf')
        for x, y in sorted(points):
            if x != base_x:
                base_x = x
                y_for_base_x = []
            for prev_base_x in y_for_base_x:
                if y in base_x_to_y[prev_base_x]:
                    w = x - base_x_to_y[prev_base_x][y]
                    h = y - prev_base_x
                    area = w * h
                    min_area = min(min_area, area)
                base_x_to_y[prev_base_x][y] = x
            y_for_base_x.append(y)
        return min_area if min_area < float('inf') else 0
