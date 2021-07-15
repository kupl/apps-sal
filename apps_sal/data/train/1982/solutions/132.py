class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        color = {}
        
        graph = collections.defaultdict(list)
        for pair in dislikes:
            p1, p2 = pair[0], pair[1]
            graph[p1].append(p2)
            graph[p2].append(p1)
        
        def dfs(node):
            for nei in graph[node]:
                if nei in color:
                    if color[nei] == color[node]:
                        return False
                else:
                    color[nei] = 1 - color[node]
                    if not dfs(nei):
                        return False
            return True
        
        for i in range(N):
            if i not in color:
                color[i] = 1
                if not dfs(i):
                    return False
        return True

