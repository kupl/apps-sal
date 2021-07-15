class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        by_x = defaultdict(set)
        by_y = defaultdict(set)
        for x, y in points:
            by_x[x].add(y)
            by_y[y].add(x)
        min_area = float(\"inf\")
        for x, ys in by_x.items():
            if len(ys) < 2:
                continue
            for y1 in ys:
                for y2 in ys:
                    if y1 == y2:
                        continue
                    valid_xs = by_y[y1] & by_y[y2]
                    for other_x in valid_xs:
                        if other_x == x:
                            continue
                        min_area = min(min_area, abs(x - other_x) * abs(y1 - y2))
        if min_area == float(\"inf\"):
            return 0
        else:
            return min_area
