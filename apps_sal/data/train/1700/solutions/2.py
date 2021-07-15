class DynamicConnectivity:
    def __init__(self, n):
        self.roots = {}
        self.sizes = {}

    def find_root(self, x):
        if not x in self.roots:
            self.roots[x] = x
            self.sizes[x] = 1
        while x != self.roots[x]:
            self.roots[x] = self.roots[self.roots[x]]
            x = self.roots[x]
        return x

    def union(self, a, b):
        a, b = self.find_root(a), self.find_root(b)
        if a == b:
            return
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        self.roots[b] = a
        self.sizes[a] += self.sizes[b]
    
    def connected(self, a, b):
        return self.find_root(a) == self.find_root(b)
