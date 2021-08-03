class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        L = len(points)
        parent = {i:i for i in range(L)}
        
        def find(p):
            if parent[p] == p:
                return p
            return find(parent[p])
        
        def union(p,q):
            if p != q:
                if p < q:
                    parent[q] = p
                else:
                    parent[p] = q
\t\t
        cost = 0
        con = {}
        count = 0            
        for i,p1 in enumerate(points):
            for j,p2 in enumerate(points):
                if i!=j and (j,i) not in con.keys():
                    d = self.dis(p1,p2)
                    con[(i,j)] = d
        k = sorted(con, key = lambda x :con[x])
        for e in k:
            x,y = e[0],e[1]
            x_set, y_set = find(x), find(y)
            if x_set!=y_set:
                union(x_set,y_set)
                count += 1
                cost += con[e]
            if count == L-1:
                break
        return cost
            
    def dis(self, p, x):
        d = abs(x[1]-p[1]) + abs(x[0]-p[0])
        return d
