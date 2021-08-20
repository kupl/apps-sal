class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        types = [[] for _ in range(3)]
        for (t, *edge) in edges:
            types[t - 1].append(edge)
        removed = 0
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        for (u, v) in types[2]:
            if self.isConnected(u, v):
                removed += 1
                continue
            self.union(u, v)
        self.parent_copy = list(self.parent)
        self.size_copy = list(self.size)
        for (u, v) in types[0]:
            if self.isConnected(u, v):
                removed += 1
                continue
            self.union(u, v)
        if sum([i == self.parent[i] for i in range(1, n + 1)]) > 1:
            return -1
        self.parent = self.parent_copy
        self.size = self.size_copy
        for (u, v) in types[1]:
            if self.isConnected(u, v):
                removed += 1
                continue
            self.union(u, v)
        if sum([i == self.parent[i] for i in range(1, n + 1)]) > 1:
            return -1
        return removed

    def isConnected(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.size[root_a] > self.size[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            return True
        return False

    def find(self, a):
        curr = a
        while self.parent[curr] != curr:
            curr = self.parent[curr]
        (root, curr) = (curr, a)
        while self.parent[curr] != curr:
            (self.parent[curr], curr) = (root, self.parent[curr])
        return root
