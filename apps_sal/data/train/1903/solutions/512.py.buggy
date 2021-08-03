class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 0
        d=collections.defaultdict(int)
        dmn=collections.defaultdict(int)
        n=len(points)
        def distance(a,b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        res=0
        start=[0,float(\"inf\")]
        for i in range(n):
            dmn[i]=0
            for j in range(i+1,n):
                t=distance(points[i],points[j])
                d[(i,j)]=t
                d[(j,i)]=t
                if d[(i,j)]<start[1]:
                    start[1]=d[(i,j)]
                    start[0]=(i,j)
        a=start[0][0]
        b=start[0][1]
        del dmn[a]
        del dmn[b]
        res+=start[1]
        
        for k in dmn.keys():
            dmn[k]=min(d[(k,a)],d[(k,b)])
        n-=2
        
        while n>0:
            nxDistance=float(\"inf\")
            for k in dmn.keys():
                if dmn[k]<nxDistance:
                    nx=k
                    nxDistance=dmn[k]
            res+=nxDistance
            del dmn[nx]
            for k in dmn.keys():
                dmn[k]=min(dmn[k],d[(k,nx)])
            n-=1
        return res
                        
