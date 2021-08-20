class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_dict = collections.defaultdict(list)
        for (x, y) in points:
            points_dict[x].append(y)
        points_dict = dict(sorted(list(points_dict.items()), key=lambda x: x[0]))
        seen_ys = dict()
        result = float('inf')
        for x in list(points_dict.keys()):
            ys = sorted(points_dict[x])
            print((x, ys))
            for (i, y2) in enumerate(ys):
                for j in range(i):
                    y1 = ys[j]
                    if (y1, y2) in seen_ys:
                        result = min(result, (y2 - y1) * (x - seen_ys[y1, y2]))
                    seen_ys[y1, y2] = x
        return result if result < float('inf') else 0
