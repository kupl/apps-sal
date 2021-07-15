class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=[]

        def getDistance(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                graph.append((i,j,getDistance(points[i],points[j])))
            
        
        graph.sort(key = lambda x: x[2])
        
        rank=[1]*len(points)
        parent=list(range(len(points)))
        
        def getParent(parent, n):
            if parent[n]==n:
                return n
            value=getParent(parent,parent[n])
            parent[n]=value
            return value
        
        def union(parent,rank,n1,n2):
            if rank[n1]>=rank[n2]:
                parent[n2]=n1
                rank[n1]+=rank[n2]
            else:
                parent[n1]=n2
                rank[n2]+=rank[n1]
                
        min_cost=0
        
        for edge in graph:
            
            u,v,cost=edge
            
            paru=getParent(parent,u)
            parv=getParent(parent,v)
            
            if parv!=paru:
                min_cost+=cost
                union(parent,rank,paru,parv)
        return min_cost
            
            

