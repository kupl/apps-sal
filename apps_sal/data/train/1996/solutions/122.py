class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        w,g,b = 0,1,2
        color = collections.defaultdict(int)
        def dfs(node):
            if color[node] != w:
                return color[node] == b
            color[node] = g
            for child in graph[node]:
                if color[child] == b:
                    continue
                elif color[child] == g or not dfs(child):
                    return False
            color[node] = b
            return True
        ans = []
        for i in range(len(graph)):
            if dfs(i) == True:
                ans.append(i)
        return ans
