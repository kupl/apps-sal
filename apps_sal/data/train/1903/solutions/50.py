class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        def find(x):
            if par[x]==x:
                return x
            par[x]=find(par[x])
            return par[x]
        def union(x,y):
            a,b=find(x),find(y)
            
            if a==b:
                return False
            par[a]=b
            return True
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                edges.append([abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j])
        edges.sort()
       
        par=[i for i in range(n)]
        ans=0
        for i in edges:
            d,u,v=i[0],i[1],i[2]
            if union(u,v):
                ans+=d
           
        return ans
