class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr == yr: return
        
        if self.size[xr] >= self.size[yr]:
            self.size[xr] += self.size[yr]
            self.size[yr] = self.size[xr]
            self.parent[yr] = xr
        else:
            self.size[yr] += self.size[xr]
            self.size[xr] = self.size[yr]
            self.parent[xr] = yr


class Solution(object):
    
    def dfs(self, u, allowed_types, visited, graph):
        visited.add(u)
        for v in graph[u]:
            if v not in visited and (allowed_types[0] in graph[u][v] or allowed_types[1] in graph[u][v]):
                self.dfs(v, allowed_types, visited, graph)
            
    
    def maxNumEdgesToRemove(self, N, edges):
        \"\"\"
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        \"\"\"
        dsu_alice = DSU(N)
        dsu_bob = DSU(N)
        count_edges = 0
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 3:
                pu, pv = dsu_bob.find(u), dsu_bob.find(v)
                if pu != pv:
                    dsu_alice.union(u, v)
                    dsu_bob.union(u, v)
                    count_edges += 1
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                pu, pv = dsu_alice.find(u), dsu_alice.find(v)
                if pu != pv:
                    dsu_alice.union(u, v)
                    count_edges += 1
            elif t == 2:
                pu, pv = dsu_bob.find(u), dsu_bob.find(v)
                if pu != pv:
                    dsu_bob.union(u, v)
                    count_edges += 1
                    
        try:
            dsu_bob.size.index(N)
            dsu_alice.size.index(N)
        except:
            return -1
        
        return len(edges) -  count_edges
        
        
