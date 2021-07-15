from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        for i in range(len(graph)):
            g[i] = graph[i]
            
        array = [False]*len(graph)
        visited = [False]*len(graph)
        
        for i in range(len(graph)):
            if visited[i]==False:
                self.dfs(i,graph,visited,array)
                
        ans = []
        for i in range(len(array)):
            if array[i]==True:
                ans.append(i)
        return ans
        
        
    def dfs(self,node,graph,visited,array):
        
        visited[node] = True
        if len(graph[node])==0:
            array[node]=True
        
        else:
            b = True
            for ver in graph[node]:
                if visited[ver] ==False:
                    self.dfs(ver,graph,visited,array)
                b = b&array[ver]
            array[node] = b
            

