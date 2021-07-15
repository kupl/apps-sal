class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dis, i, j))
        
        UF = {i: i for i in range(n)}
        def find(i):
            if i != UF[i]:
                UF[i] = find(UF[i])
            return UF[i]
        def union(i, j):
            UF[find(i)] = find(j)
            
        ans = 0
        for w, x, y in sorted(edges):
            if find(x) != find(y):
                ans += w
                union(x, y)
        return ans
