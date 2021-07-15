class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(i):
            if color[i] != 0: return color[i]
            color[i] = 1
            if any(dfs(j)==1 for j in graph[i]):
                return color[i]
            color[i] = 2
            return color[i]
            
        color = collections.defaultdict(int)
            
        ans = []
        n = len(graph)
        for i in range(n):
            if dfs(i) == 2:
                ans.append(i)
                
        return ans
                

