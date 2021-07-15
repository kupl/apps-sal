class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        L = len(points)
        res = 0
        con = {}
        father = {i:i for i in range(L)}
        def find(pidx):
            if father[pidx] == pidx:
                return pidx
            return find(father[pidx])
        def union(p,q):
            if p != q:
                if p < q:
                    father[q] = p
                else:
                    father[p] = q
        for i,p in enumerate(points):
            for j,p2 in enumerate(points):
                if i!=j and (j,i) not in list(con.keys()):
                    d = self.dis(p,p2)
                    con[(i,j)] = d
        k = sorted(con, key = lambda x :con[x])
        for e in k:
            x,y = e[0],e[1]
            fx, fy= find(x), find(y)
            if fx!=fy:
                union(fx,fy)
                res += con[e]
        return res
            
    def dis(self, p, x):
        d = abs(x[1]-p[1]) + abs(x[0]-p[0])
        return d

