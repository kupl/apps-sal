class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def dist(e1, e2):
            return abs(e1[0]-e2[0])+abs(e1[1]-e2[1])
        
        def find(x):
            while x in uf:
                # path compress
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        
        def union(x,y):
            px,py = find(x), find(y)
            if px==py: return False
            uf[px] = py
            return True
        
        n = len(points)
        res = 0
        uf = {}
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                edges.append([dist(points[i],points[j]),i,j])
                
        edges.sort()
        for cost,x,y in edges:
            if union(x,y):
                res += cost
                
        return res
