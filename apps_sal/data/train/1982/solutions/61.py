class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)          
        def dfs(graph, colorGraph, node, color):
            colorGraph[node] = color
            for adj in graph[node]:
                if colorGraph[adj] == color:
                    return False
                if colorGraph[adj] == 0:
                    if not dfs(graph, colorGraph, adj, -color):
                        return False
            return True     
        colorGraph=[0]*(N+1)  
        for i in range(1,N):
            if colorGraph[i] == 0:
                if not dfs(graph, colorGraph, i, 1):
                    return False
        return True
