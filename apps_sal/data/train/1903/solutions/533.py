class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def method1():
            class UF:
                def __init__(self,size):
                    self.p=list(range(size))
                    self.rank=[1]*size
                    
                def find(self,x):
                    if x!=self.p[x]:
                        self.p[x]=self.find(self.p[x])
                    return self.p[x]
                
                def union(self,x,y):
                    px=self.find(x)
                    py=self.find(y)
                    
                    if self.rank[px]<self.rank[py]:
                        px,py=py,px
                    
                    self.p[px]=py
                    if self.rank[px]==self.rank[py]:
                        self.rank[px]+=1
                        
            edges=[]
            n=len(points)
            
            for i in range(n-1):
                for j in range(i+1,n):
                    dist=abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                    edges.append((dist,i,j))
                        
            edges.sort()
        
            uf=UF(n)
            res=0
            for cost, u, v in edges:
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    res += cost
        
            return res
        return method1()
                    
            

