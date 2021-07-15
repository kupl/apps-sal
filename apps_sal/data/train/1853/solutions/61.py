from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], cap: int) -> int:
        
        minDistance = collections.defaultdict(lambda: collections.defaultdict(lambda: float(\"inf\")))
        
        for i in range(n):
            minDistance[i][i]=0
        
        for i,j,w in edges:
            minDistance[i][j]=w
            minDistance[j][i]=w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    minDistance[i][j]=min(minDistance[i][j],minDistance[i][k]+minDistance[k][j])
        
        mi=float(\"inf\")
        ans=-1
        
        for i in range(n):
            neighCount=sum(minDistance[i][j]<=cap for j in range(n) if j!=i)
            if(neighCount<=mi):
                mi=neighCount
                ans=i
        return ans
        
        
        
        
        
        
        
        
        
        
        
#         graph=defaultdict(list)
        
#         for i in edges:
#             graph[i[0]].append([i[1],i[2]])
#             graph[i[1]].append([i[0],i[2]])
            
#         # print(graph)
#         self.ans=-1
#         self.mi=float('inf')
#         def bfs(parent):
#             seen={parent:-1}
#             q=[(parent,0)]
#             while(q!=[]):
#                 tem_node,used=q.pop(0)
#                 for node,dist in graph[tem_node]:
#                     if((node not in seen or dist+used<seen[node]) and (dist+used)<=cap):
#                         q.append((node,dist+used))
#                         seen[node]=dist+used
#             if(self.mi>len(seen)):
#                 self.mi=len(seen)
#                 self.ans=parent
#             elif(self.mi==len(seen) and parent>self.ans):
#                 self.ans=parent
        
#         for i in range(n):
#             bfs(i)
            
#         return self.ans
        
        
        
        
        
#         di=dict()
#         for i in range(n):
#             di[i]=set()
        
#         print(graph)
#         # self.mi=float('inf')
#         # self.node=-1
#         def dfs(node,thres,covered,parent):
#             if(thres<0):
#                 return
#             di[parent].add(node)
#             for i in graph[node]:
#                 dfs(i[0],thres-i[1],covered+1,parent)
            
        
#         for i in range(n):
#             dfs(i,distanceThreshold,0,i)
#         ans=-1
#         mi=float('inf')
#         print(di)
#         for i,j in di.items():
#             if(len(j)-1<mi):
#                 mi=len(j)-1
#                 ans=i
#             elif(len(j)-1==mi):
#                 ans=i
#         return ans
        
        
        # return self.node
