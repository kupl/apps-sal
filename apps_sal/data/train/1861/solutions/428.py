class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        lastx = {}
        everyx = collections.defaultdict(list)
        min_area = math.inf
        for x, y in points:
            everyx[x].append(y)
        for x in sorted(everyx):
            everyy = sorted(everyx[x])
            for i, y1 in enumerate(everyy):
                for j in range(i):
                    y2 = everyy[j]
                    if (y1, y2) in lastx:
                        area = abs(y2 - y1) * abs(x - lastx[y1, y2])
                        min_area = min(area, min_area)
                    lastx[y1, y2] = x
        return min_area if min_area < math.inf else 0
