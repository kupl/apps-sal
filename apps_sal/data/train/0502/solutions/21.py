class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        visited = [False] * len(graph)
        sizes = [0] * len(graph)
        for node in range(len(graph)):
            if visited[node]:
                continue
            vertices = []
            numOfInitials = self.dfs(graph, node, visited, vertices, initial)
            size = len(vertices)
            for i in vertices:
                sizes[i] = size if numOfInitials < 2 else 0
        maxSpread = -1
        maxNode = -1
        for i in initial:
            print(i)
            if sizes[i] > maxSpread:
                maxSpread = sizes[i]
                maxNode = i
            elif sizes[i] == maxSpread:
                maxNode = min(maxNode, i)
        return maxNode
    
    def dfs(self, graph, node, visited, vertices, initial):
        initials = 0
        if visited[node]:
            return initials
        vertices.append(node)
        visited[node] = True
        if node in initial:
            initials += 1
        for i in range(len(graph[node])):
            if graph[node][i] == 1:
                initials += self.dfs(graph, i, visited, vertices, initial)
        return initials
        

