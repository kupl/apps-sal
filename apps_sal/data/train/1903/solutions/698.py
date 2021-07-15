class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n=len(p)
        a=[i for i in range(n+1)]
        rank=[0 for i in range(n+1)]
        def find(i):
            if i==a[i]:
                return i
            a[i]=find(a[i])
            return a[i]
        def union(x,y):
            xs=find(x)
            ys=find(y)
            if xs!=ys:
                if rank[ys]>rank[xs]:
                    ys,xs=xs,ys
                a[ys]=xs
                rank[xs]+=1
                return 1
            return 0
        edge=[]
        for i in range(n):
            for j in range(i+1,n):
                dis=abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])
                edge.append([dis,i,j])
        ans=0
        edge.sort()
        for dis,i,j in edge:
            if union(i,j):
                ans+=dis
        return ans        
                

