class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True


class Solution:
    def minCostConnectPoints(self, P: List[List[int]]) -> int:
        from collections import defaultdict
        #G = defaultdict(set)
        connections = []
        for i in range(len(P)):
            for j in range(i+1, len(P)):
                if i != j:
                    cost = abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1])
                    #G[i].add((j, cost))
                    #G[j].add((i, cost))
                    connections.append([i,j,cost])
        #print(connections)
        #print(len(connections))
        connections = list(connections)
        connections.sort(key = lambda x : x[2])
        dsu = DSU(len(P))
        res = 0
        for u,v,w in connections:
            curr = dsu.union(u,v)
            if curr:
                res += w
        return res

