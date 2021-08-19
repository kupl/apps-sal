class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n = len(a)
        g = defaultdict(set)

        @lru_cache(None)
        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = a[i]
                x2, y2 = a[j]
                w = dist(x1, y1, x2, y2)
                g[(x1, y1)].add((w, x2, y2))
                g[(x2, y2)].add((w, x1, y1))

        q = [(0, (a[0][0], a[0][-1]))]
        visited = set()
        total = ct = 0
        while q:
            # for _ in range(len(q)):
            c, (x1, y1) = heapq.heappop(q)
            if (x1, y1) in visited:
                continue
            visited.add((x1, y1))
            total += c
            ct += 1
            for w, x2, y2 in g[(x1, y1)]:
                heapq.heappush(q, (w, (x2, y2)))
            if ct >= n:
                break
        return total
