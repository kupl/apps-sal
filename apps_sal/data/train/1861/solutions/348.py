class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        _set = {(x, y) for (x, y) in points}
        res = math.inf
        for (p1, p2) in combinations(points, 2):
            arr = [p1, p2]
            arr.sort()
            ((x1, y1), (x2, y2)) = arr
            (l, w) = (y2 - y1, x2 - x1)
            if l > 0 and w > 0 and ((x1, y1 + l) in _set) and ((x1 + w, y1) in _set):
                res = min(res, l * w)
        return 0 if math.isinf(res) else res
