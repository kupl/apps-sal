#Cycle detection alg: s f pointers are only for lists and linkedlists. WGB DFS is for graph.
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0]*(len(graph)) #0 white, 1 grey, 2 black
        
        def df(v):
            if color[v]==2:
                return True
            if color[v]==1: #Grey nodes will stay grey if cycle found. THis is for when doing WGB DFS for every node.
                return False 
            
            color[v] = 1 #set it to grey while traversing
            for v2 in graph[v]:
                if color[v2]==1 or color[v2]==0 and not df(v2):
                    return False       
            color[v] = 2 #set it to black after traversing if safe
            
            return True
        
        safe = []
        for v in range(len(graph)):
            if df(v):
                safe.append(v)
        
        return safe
        

