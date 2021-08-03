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
                if n1 < n2:
                    par[n2] = n1
                else:
                    par[n1] = n2
                return True
            else:
                return False
        arr = []
        for i in range(len(points)):
            _min = 10e9
            ix = -1
            for j in range(i + 1, len(points)):
                n = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                arr.append((n, (i, j)))
# print(ans)
# arr=list(arr)
        arr.sort()
        for x in arr:
            i = x[1][0]
            j = x[1][1]
            n1 = find(i)
            n2 = find(j)
            if n1 != n2:
                if n1 < n2:
                    par[n2] = n1
                else:
                    par[n1] = n2
                ans += x[0]
        return ans
