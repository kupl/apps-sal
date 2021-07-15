class Solution:
    def dfs(self, node, v, g):
        if v[node]==2:
            return False
        if v[node]==1:
            return True
        if len(g[node])==0:
            v[node]=2
            return False
        v[node]=1
        for i in g[node]:
            if self.dfs(i, v, g):
                return True
        v[node]=2
        return False
    
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if len(graph)==0:
            return []
        g = {}
        v = [0]*len(graph)
        ans = set()
        
        for i in range(len(graph)):
            if not self.dfs(i, v, graph):
                ans.add(i)
        ans = list(ans)
        ans.sort()
        return ans
