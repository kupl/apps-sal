class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=[[99999 for j in range(n)]for k in range(n)]
        dict1={}
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        for i in range(n):
            graph[i][i]=1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
        ans=-1
        min1=999999999
        for i in range(n):
            count=0
            for j in range(n):
                if(graph[i][j] <= distanceThreshold):
                    count+=1
            #print(count)
            if(count <= min1):
                min1=count
                ans=i
        return ans

