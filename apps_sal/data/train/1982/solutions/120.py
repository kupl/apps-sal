class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)          
        def dfs(graph, color, node, col):
            color[node] = col
            for neigh in graph[node]:
                if color[neigh] == col:
                    return False
                if color[neigh] == 0:
                    if not dfs(graph, color, neigh, -col):
                        return False
            return True     
        color = [0] * (N+1)  
        for i in range(1,N):
            if color[i] == 0:
                if not dfs(graph, color, i, 1):
                    return False
        return True
