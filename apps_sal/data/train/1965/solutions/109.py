class Solution:
    def __init__(self):
        self.n = 0
        self.used = []

    def dfs(self, edges, i):
        self.used[i] = True
        for edge in edges[i]:
            if self.used[edge] == False:
                self.dfs(edges, edge)

    def iterate(self, edges):
        self.used = [False for i in range(self.n)]
        components = 0
        for i in range(self.n):
            if self.used[i] == True:
                continue
            self.dfs(edges, i)
            components += 1
        return components

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.n = n
        alice = [[] for i in range(self.n)]
        bob = [[] for i in range(self.n)]
        both = [[] for i in range(self.n)]
        bothCount = 0
        tot = len(edges)
        for edge in edges:
            if edge[0] == 1:
                alice[edge[1] - 1].append(edge[2] - 1)
                alice[edge[2] - 1].append(edge[1] - 1)
            if edge[0] == 2:
                bob[edge[1] - 1].append(edge[2] - 1)
                bob[edge[2] - 1].append(edge[1] - 1)
            if edge[0] == 3:
                bob[edge[1] - 1].append(edge[2] - 1)
                bob[edge[2] - 1].append(edge[1] - 1)
                alice[edge[1] - 1].append(edge[2] - 1)
                alice[edge[2] - 1].append(edge[1] - 1)
                both[edge[1] - 1].append(edge[2] - 1)
                both[edge[2] - 1].append(edge[1] - 1)
                bothCount += 1
        if self.iterate(alice) != 1 or self.iterate(bob) != 1:
            return -1
        bothComponents = self.iterate(both)
        needed = self.n - bothComponents
        needed += 2 * (bothComponents - 1)
        return tot - needed
