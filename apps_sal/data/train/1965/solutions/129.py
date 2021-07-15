class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU()
        bob = DSU()
        res = 0
        for t, u, v in edges:
            if t == 3:
                if alice.find(u) == alice.find(v):
                    res += 1
                else:
                    alice.union(u, v)
                    bob.union(u, v)
                    
        for t, u, v in edges:
            if t == 1:
                if alice.find(u) == alice.find(v):
                    res += 1
                else:
                    alice.union(u, v)
            if t == 2:
                if bob.find(u) == bob.find(v):
                    res += 1       
                else:
                    bob.union(u, v)
                    
        if max(bob.count.values()) != n or max(alice.count.values()) != n:
            return -1
        
        return res
        
class DSU:
    def __init__(self):
        self.father = {}
        self.count = {}
    
    def find(self, a):
        self.father.setdefault(a, a)
        self.count.setdefault(a, 1)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]
    
    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = self.father[_b]
            self.count[_b] += self.count[_a]
