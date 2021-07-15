class UnionSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}
        # self.level = {i:0 for i in range(1, n+1)}
    
    def union(self, i, j):
        # if self.level[i] < self.level[j]:
        self.parent[self.get(i)] = self.get(j)
        
    def get(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get(self.parent[i])
            return self.parent[i]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
                    
        mapping = {k: [] for k in range(1, 4)}
        alice = UnionSet(n)
        bob = UnionSet(n)
        for t, u, v in edges:
            mapping[t].append((v, u))

        
        for u, v in mapping[3]:
            alice.union(u, v)
        bob.parent = alice.parent.copy()
        
        seen = set()
        for i in range(1, n+1):
            seen.add(alice.get(i))
        
        after3 = len(seen)
        
        for u,v in mapping[1]:
            alice.union(u, v)
        for u, v in mapping[2]:
            bob.union(u, v)
        
        seen = set()
        for i in range(1, n+1):
            seen.add(alice.get(i))
        if len(seen) != 1:
            return -1

        seen = set()
        for i in range(1, n+1):
            seen.add(bob.get(i))
        if len(seen) != 1:
            return -1
    
    
        delete3 = len(mapping[3]) - (n - after3)
        use3 = len(mapping[3]) - delete3
        return len(mapping[1]) + len(mapping[2]) + use3 * 2 - 2 * (n - 1) + delete3
