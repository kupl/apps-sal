class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        l=[[0 for i in range(n)] for j in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                res=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                l[i][j]=res
                l[j][i]=res
        def minKey():
            m=sys.maxsize
            minind = 0
            for i in range(n):
                if key[i]<m and vis[i]==0:
                    m=key[i]
                    minind=i
            return minind
        vis=[0]*n
        key=[sys.maxsize]*n
        key[0]=0
        for i in range(n-1):
            u=minKey()
            vis[u]=1
            for v in range(n):
                if l[u][v] and vis[v]==0 and l[u][v]<key[v]:
                    key[v]=l[u][v]
        return sum(key)
