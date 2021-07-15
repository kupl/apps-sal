class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * N
        graph = defaultdict(set) 
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        
        counts = [1] * N
        ans = [0] * N
        self.dfs_root(graph, 0, 0, counts, ans)
        self.dfs_child(graph, 0, 0, counts, ans, N)
        visited = {}
        return [self.dfs(graph, i, -1, visited)[0] for i in range(N)]
    
    def dfs(self, graph, node, parent, visited):
        if (node, parent) in visited:
            return visited[node, parent]
        distance, count = 0, 1
        for child in graph[node]:
            if child != parent:
                d, c = self.dfs(graph, child, node, visited)
                distance += d + c
                count += c
        visited[node, parent]  = (distance, count)
        return distance, count
        
        
    def dfs_root(self, graph, root, parent, counts, ans):
        for child in graph[root]:
            if child != parent:
                self.dfs_root(graph, child, root, counts, ans)
                counts[root] += counts[child]
                ans[root] += ans[child] + counts[child]
            
    def dfs_child(self, graph, root, parent, counts, ans, N):
        for child in graph[root]:
            if child != parent:
                ans[child] = (N -  counts[child]) + ans[root] - counts[child]
                self.dfs_child(graph, child, root, counts, ans, N) 
