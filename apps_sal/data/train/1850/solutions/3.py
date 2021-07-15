class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        import collections
        self.graph = collections.defaultdict(set)
        for u, v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)
        self.count = [1 for _ in range(N)]
        self.sums = [0 for _ in range(N)]
        self.dfs(0, None)
        self.dfs1(0, None, N)
        return self.sums
    
    def dfs(self, node, parent):
        for child in self.graph[node]:
            if child == parent:
                continue
            self.dfs(child, node)
            self.count[node] += self.count[child]
            self.sums[node] += self.sums[child] + self.count[child]
    
    def dfs1(self, node, parent, N):
        for child in self.graph[node]:
            if child == parent:
                continue
            self.sums[child] = self.sums[node] + N - 2*self.count[child]
            self.dfs1(child, node, N)


