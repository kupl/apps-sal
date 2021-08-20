class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        h = defaultdict(deque)
        v = defaultdict(deque)
        p = set([(x, y) for (x, y) in points])
        for (x, y) in points:
            h[x].append(y)
            v[y].append(x)
        minArea = float('inf')
        for (x, y) in points:
            for y1 in h[x]:
                if y1 != y:
                    for x1 in v[y]:
                        if x1 != x:
                            if (x1, y1) in p:
                                minArea = min(minArea, abs(y1 - y) * abs(x1 - x))
            if h[x]:
                h[x].popleft()
            if v[y]:
                v[y].popleft()
        if minArea == float('inf'):
            return 0
        return minArea
