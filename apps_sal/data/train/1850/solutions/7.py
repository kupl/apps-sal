class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.N = N
        self.childnum = [0] * self.N
        self.cdist = [0] * self.N
        self.neighbors = []
        for i in range(N):
            self.neighbors.append(set())

        for e in edges:
            self.neighbors[e[0]].add(e[1])
            self.neighbors[e[1]].add(e[0])

        self.visit(0, set([-1]))
        self.visit2(0, set([-1]))
        return self.cdist

    def visit2(self, node, pre):
        children = self.neighbors[node] - pre
        pre = pre.pop()
        if pre != -1:
            self.cdist[node] = self.cdist[pre] + self.N - 2 * (self.childnum[node] + 1)
        for c in children:
            self.visit2(c, set([node]))

    def visit(self, node, pre):
        children = self.neighbors[node] - pre
        for c in children:
            self.visit(c, set([node]))
        for c in children:
            self.childnum[node] += self.childnum[c] + 1
            self.cdist[node] += self.cdist[c]

        self.cdist[node] += self.childnum[node]
