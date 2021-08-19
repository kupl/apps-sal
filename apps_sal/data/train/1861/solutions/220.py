class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xs = collections.defaultdict(set)
        ys = collections.defaultdict(set)
        for point in points:
            x, y = point[0], point[1]
            xs[x].add(y)
            ys[y].add(x)
        area = 40000 ** 2 + 1
        for x in xs:
            for y1, y2 in itertools.product(xs[x], xs[x]):
                if y1 <= y2:
                    continue
                #print(f'x={x}, y1={y1}, y2={y2}')
                A = set(xx for xx in ys[y1] & ys[y2] if xx < x)
                #print('A=', A)
                if len(A) > 0:
                    area = min(area, (y1 - y2) * (x - max(A)))
        return 0 if area == 40000 ** 2 + 1 else area
