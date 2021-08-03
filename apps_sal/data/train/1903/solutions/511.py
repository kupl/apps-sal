def top(idx, i):
    d, j = 0, idx[i]
    while i != j:
        i, j, d = j, idx[j], d + 1
    return j, d


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        best, idx = 0, {i: i for i in range(len(points))}
        buf = [(abs(x1 - x2) + abs(y1 - y2), i1, i2)
               for i1, (x1, y1) in enumerate(points[:-1])
               for i2, (x2, y2) in enumerate(points[i1 + 1:], i1 + 1)]
        for now, i1, i2 in sorted(buf):
            j1, d1 = top(idx, i1)
            j2, d2 = top(idx, i2)
            if j1 == j2:
                continue
            best += now
            if d1 < d2:
                idx[i1] = idx[i2] = idx[j1] = j2
            else:
                idx[i1] = idx[i2] = idx[j2] = j1
        return best
