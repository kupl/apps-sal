class Solution:
    def createGraph(self,N,dislikes):
        # create undirected graph, edgeList
        adjList = {}
        
        # get base adjList
        baseSet = set()
        
        for vertex in range(1,N+1):
            adjList[vertex] = set()
            
        # remove non valid edges
        for v,v1 in dislikes:
            adjList[v].add(v1)
            adjList[v1].add(v)
        
        for i in adjList.keys(): print(i , \" \" , adjList[i])
        return adjList
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjList = self.createGraph(N,dislikes)
        
        def dfs(currentLoc,adjList,colored,color):
            colored[currentLoc] = color
            
            for adj in adjList[currentLoc]:
                if adj not in colored:
                    if not dfs(adj,adjList,colored, not color): return False
                else:
                    if colored[adj] == color: return False
                    
            return True
                    
                    
                
        colored = {}
        color = 1
        for i in range(1,N+1):
            if i not in colored:
                if not dfs(i,adjList,colored,color): return False
        return True
        
            
            
            
            
            
            
            

        
        
        
        
            
        
