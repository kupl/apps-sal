class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for w, v in dislikes:
            graph[w].append(v)
            graph[v].append(w)
        
        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])
        
        for node in range(1, N + 1):
            if node not in color:
                if dfs(node) == False:
                    return False
        return True

