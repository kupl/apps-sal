class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_grouped, y_grouped = collections.defaultdict(set), collections.defaultdict(set)

        for x, y in points:
            x_grouped[x].add(y)

        res = float(\"inf\")
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if y2 in x_grouped[x1] and y1 in x_grouped[x2]:
                    width = abs(x1 - x2)
                    height = abs(y1 - y2)
                    if width != 0 and height != 0:
                        res = min(res, width * height)

        if res < float(\"inf\"): return res
        return 0
