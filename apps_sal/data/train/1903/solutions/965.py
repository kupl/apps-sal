class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 0
        
        visited=[0]*(len(points))
        q=[]
        start=0
        for i in range(1,len(points)):
            dist=abs(points[i][0]-points[0][0])+abs(points[i][1]-points[0][1])
            q.append([dist,i])
            
        heapq.heapify(q)
        # print(q)
        visited[0]=1
        cost=0
        count=1
        while True:
            
            x=heapq.heappop(q)
            # print(x)
            if visited[x[1]]==0:
                cost=cost+x[0]
                visited[x[1]]=1
                count=count+1
            if count==len(points):
                return cost
            
            for i in range(len(points)):
                if visited[i]==0:
                    dist=abs(points[i][0]-points[x[1]][0])+abs(points[i][1]-points[x[1]][1])
                    heapq.heappush(q,[dist,i])
        
            
            
            
        
        
        
        
        
        
#         def dfs(index,visited,count):
#             if count==len(points):
#                 return 0
            
#             dist=float(\"inf\")
#             for i in range(len(points)):
#                 if visited[i]==0:
#                     visited[i]=1
#                     dist=min(dist,abs(points[i][0]-points[index][0])+abs(points[i][1]-points[index][1])+dfs(i,visited,count+1))
#                     visited[i]=0
#             visited[index]=0
#             return dist
#         visited=[0]*len(points)
#         visited[0]=1
#         x=dfs(0,visited,1)
#         return x
                    

