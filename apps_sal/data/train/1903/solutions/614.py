import sys
input = sys.stdin.readline


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import math as mt

        def re(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        ar = []
        n = len(points)
        par = [i for i in range(len(points) + 1)]

        def find(i):
            while i != par[i]:
                i = par[i]
            return par[i]

        def join(i, j):
            a = find(i)
            b = find(j)
            if a != b:
                par[a] = par[b] = min(a, b)
        for i in range(n):
            for j in range(i + 1, n):
                temp = re(points[i], points[j])
                ar.append([temp, i, j])
        ans = 0
        cnt = 0
        ar.sort()
        for (a, b, c) in ar:
            if find(b) != find(c):
                join(b, c)
                ans += a
                cnt += 1
            if cnt == n - 1:
                break
        return ans
