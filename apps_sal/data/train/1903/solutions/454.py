class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        def find(u):
                
            while parents[u]>=0:
                u = parents[u]
            
            return u
        
        def union(u,v):
             
            if parents[u]<parents[v]:
                parents[u] += parents[v]
                parents[v] = u
            
            else:
                parents[v]+=parents[u]
                parents[u]=v
                
        n = len(points)
        costs = {}
        
        for i in range(n):
            for j in range(i+1,n):
                costs[(i,j)] = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                
        sorted_costs = sorted(list(costs.items()), key=lambda cost: -cost[1])
        
        s = set()
        cost = 0
        parents = [-1]*n
        
        while sorted_costs:
            
            (u,v),weight = sorted_costs.pop()
            
            pu = find(u)
            pv = find(v)
            
            if (pu!=pv):
                union(pu,pv)
                cost+=weight
            
        return cost
    
        

