class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ll = len(points)
        if ll == 1:
            return 0
        distances = []
        def get_distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        for i in range(ll):
            for j in range(i + 1, ll):
                distances.append((get_distance(i, j), i, j))
        distances.sort()
        size = [1] * ll
        parents = list(range(ll))
    
        def ufind(x):
            if parents[x] != x:
                return ufind(parents[x])
            return x
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            if ux < uy:
                parents[ux] = uy
                size[uy] += ux
            else:
                parents[uy] = ux
                size[ux] += uy
            
        
        res = 0
        for d, x, y in distances:
            ux = ufind(x)
            uy = ufind(y)
            if ux != uy:
                uunion(ux, uy)
                res += d
        return res
                
        

