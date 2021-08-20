class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def func(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        ans = 0
        n = len(points)
        print(n)
        s = set()
        ver = [(0, (0, 0))]
        while len(s) < n:
            (res, (v1, v2)) = heapq.heappop(ver)
            if v1 in s and v2 in s:
                continue
            ans += res
            s.add(v2)
            for i in range(n):
                if i not in s and i != v2:
                    sol = func(points[i], points[v2])
                    heapq.heappush(ver, (sol, (v2, i)))
        return ans
