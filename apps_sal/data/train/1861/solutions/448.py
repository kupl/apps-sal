class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        (xs, ys) = (collections.defaultdict(set), collections.defaultdict(set))
        for (x1, y1) in points:
            for x2 in xs[y1]:
                for y2 in ys[x1]:
                    if x2 in xs[y2]:
                        res = min(res, abs(x2 - x1) * abs(y2 - y1))
            xs[y1].add(x1)
            ys[x1].add(y1)
        return res if res < float('inf') else 0
