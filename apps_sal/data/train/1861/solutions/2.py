class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        countx = len(set((x for (x, y) in points)))
        county = len(set((y for (x, y) in points)))
        if countx == n or county == n:
            return 0
        container = defaultdict(list)
        if countx > county:
            for (x, y) in points:
                container[x].append(y)
        else:
            for (x, y) in points:
                container[y].append(x)
        lastx = {}
        ans = float('inf')
        for x in sorted(container):
            container[x].sort()
            for y in range(len(container[x])):
                for z in range(y):
                    (y1, y2) = (container[x][z], container[x][y])
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
