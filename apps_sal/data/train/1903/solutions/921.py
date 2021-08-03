class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        dic = {}

        def find(i):
            dic.setdefault(i, i)
            if dic[i] != i:
                dic[i] = find(dic[i])
            return dic[i]

        def union(i, j):
            fi, fj = find(i), find(j)
            if fi != fj:
                dic[fi] = fj
                return 1
            return 0
        dis = []
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                d = distance(A[i], A[j])
                dis.append([d, i, j])
        dis = sorted(dis)
        ret, ct = 0, 0
        for d, i, j in dis:
            if union(i, j):
                ret += d
                ct += 1
                if ct == n:
                    break
        return ret
