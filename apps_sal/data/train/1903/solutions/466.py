class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        
        d = []
        for i, (xi,yi) in enumerate(points[:-1]):
            for j, (xj,yj) in enumerate(points[i+1:]):
                d.append([i,i+j+1,abs(xj-xi)+abs(yj-yi)])
        d = sorted(d, key=lambda r: r[2])
        
        father = {i:i for i in range(n)}
        def find(x):
            if x != father[x]:
                father[x] = find(father[x])
            return father[x]

        res, c = 0, 0
        for i,j,distance in d:
            if find(i) != find(j):
                father[find(i)] = j
                res += distance
                c += 1
                if c == n-1:
                    return res
            

