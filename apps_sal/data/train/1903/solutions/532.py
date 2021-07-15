import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l=len(points)
        stc=[]
        heapq.heapify(stc)
        cost=0
        self.parent=[-1 for i in range(l)]
        
        def find(a):
            if self.parent[a]<0:
                print(('a ',a))
                return a
            else:
                return find(self.parent[a])
        
        
        
        def union(a,b):
            u=find(a)
            v=find(b)
            if u==v:
                return False
            else:
                if abs(self.parent[u])>=abs(self.parent[v]):
                    self.parent[u]+=self.parent[v]
                    self.parent[v]=u
                else:
                    self.parent[v]+=self.parent[u]
                    self.parent[u]=v
                return True
        
        
        
        
        for i in range(l):
            for j in range(l):
                if i!=j:
                    heapq.heappush(stc,[abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j])         
        edge=0
        while(edge<l-1):
            t=heapq.heappop(stc)
            y=union(t[1],t[2])
            if y==True:
                cost+=t[0]
                edge+=1
        return cost
                    
        
        
        
        
        

