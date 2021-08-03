class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n = len(a)
        if n <= 1:
            return 0
        d, cur, min_d = dict(), set(), float('inf')
        for i in range(n - 1):
            for j in range(n):
                d[i, j] = d[j, i] = abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1])
                if min_d > d[i, j]:
                    min_d = d[i, j]
                    cur = set([i, j])

        rem, cand = set(range(n)) - cur, []
        for x in cur:
            for y in rem:
                cand.append((d[(x, y)], x, y))

        heapify(cand)
        ans = min_d
        while len(cur) < n:
            val, x, y = heappop(cand)
            if y not in cur:
                cur.add(y)
                rem.discard(y)
                ans += val
                for z in rem:
                    heappush(cand, (d[(y, z)], y, z))
        return ans
