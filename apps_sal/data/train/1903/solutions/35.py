class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:return 0
        ans=0
        par={}
        def find(x):
            if x not in par:return x
            res=find(par[x])
            par[x]=res
            return res
        def union(a,b):
            n1=find(a)
            n2=find(b)
            if n1!=n2:
                if n1<n2:
                    par[n2]=n1
                else:
                    par[n1]=n2
                return True
            else:return False
        arr=set()
        for i in range(len(points)):
            _min=10e9
            ix=-1
            for j in range(len(points)):
                if i!=j:
                    n=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    arr.add((n,(min(i,j),max(i,j))))
                    if n<_min:
                        ix=j
                        _min=n
            if union(i,ix):
                ans+=_min
        arr=list(arr)
        arr.sort()
        for x in arr:
            i=x[1][0]
            j=x[1][1]
            n1=find(i)
            n2=find(j)
            if n1!=n2:
                union(i,j)
                ans+=x[0]
        return ans         
