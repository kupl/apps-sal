class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ln=len(points)
        if ln<=1:return 0
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
        arr=[]
        for i in range(ln):
            t1=points[i]
            for j in range(i+1,ln):
                t2=points[j]
                n=abs(t1[0]-t2[0])+abs(t1[1]-t2[1])
                arr.append((n,i,j))
        arr.sort()
        for x in arr:
            i=x[1]
            j=x[2]
            n1=find(i)
            n2=find(j)
            if n1!=n2:
                if n1<n2:
                    par[n2]=n1
                else:
                    par[n1]=n2
                ans+=x[0]
        return ans   
