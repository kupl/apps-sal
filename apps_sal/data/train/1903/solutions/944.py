class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        ans = 0
        par = {}

        def find(x):
            if x not in par:
                return x
            res = find(par[x])
            par[x] = res
            return res

        def union(a, b):
            n1 = find(a)
            n2 = find(b)
            if n1 != n2:
                if n1 <= n2:
                    par[n2] = n1
                else:
                    par[n1] = n2
                return True
            else:
                return False
        arr = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                n = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                arr.append((n, (i, j)))
        arr.sort()
        for x in arr:
            i = x[1][0]
            j = x[1][1]
            if union(i, j):
                ans += x[0]

        return ans
