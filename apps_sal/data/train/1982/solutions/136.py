class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict
        def build_graph():
            graph = defaultdict(set)
            for u, v in dislikes:
                graph[u].add(v)
                graph[v].add(u)
            return graph
        
        
        def dfs(node, next_color):
            if node in color: return color[node] == next_color
            color[node] = next_color
            for nei in graph[node]:
                if not dfs(nei, next_color^1):
                    return False
            return True
            
        graph = build_graph()
        color = {}
        for node in graph:
            if node not in color:
                if not dfs(node, 0): return False
        return True
