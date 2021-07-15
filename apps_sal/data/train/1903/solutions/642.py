class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        uf=list(range(n))
        def find(x):
            if uf[x]!=x:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            uf[find(x)]=find(y)
        costs=[]
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1=points[i]
                x2,y2=points[j]
                cost=abs(x1-x2)+abs(y1-y2)
                costs.append([cost,i,j])
        costs.sort()
        res=0
        for cost,i,j in costs:
            if find(i)!=find(j):
                union(i,j)
                res+=cost
        return res
