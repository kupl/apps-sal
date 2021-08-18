class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        lines = self.find_lines(points)
        min_area = 0
        d = {}
        for x, ys in lines:
            if ys in d:
                px = d[ys]
                curr_min_area = abs(x - px) * abs(ys[0] - ys[1])
                min_area = min(min_area, curr_min_area) if min_area > 0 else curr_min_area
            d[ys] = x
        return min_area

    def find_lines(self, points: List[List[int]]) -> List[Tuple[int, Tuple[int, int]]]:
        ps = defaultdict(list)
        for x, y in sorted(points):
            ps[x].append(y)
        lines = []
        for x, ys in ps.items():
            for i, y0 in enumerate(ys):
                for y1 in ys[i + 1:]:
                    lines.append((x, (y0, y1)))
        return lines
