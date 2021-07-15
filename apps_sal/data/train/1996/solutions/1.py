class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        N = len(graph)
        if N == 0:
            return []
        
        color = [0] * N
        in_cycle = set()
        
        def dfs(i):
            if color[i] != 0:
                return color[i] == 2
            
            color[i] = 1
            for j in graph[i]:
                if color[j] == 2:
                    continue
                elif color[j] == 1 or (dfs(j) == False):
                    return False
            color[i] = 2
            return True
        
        ret = []
        for i in range(N):
            if dfs(i):
                ret.append(i)
        return ret
        

