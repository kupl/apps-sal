class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = UnionFind(n)
        bob = UnionFind(n)
        
        remove = 0
        for t, u, v in edges:
            if t == 3:
                aliceMerge = alice.union(u, v)
                bobMerge = bob.union(u, v)
                if not aliceMerge and not bobMerge:
                    remove += 1
                
        for t, u, v in edges:
            if t != 3 and not alice.union(u, v) and not bob.union(u, v):
                remove += 1
                
        if alice.num_of_components != 1 or bob.num_of_components != 1:
            return -1
        
        return remove

class UnionFind:
    
    def __init__(self, n):
        self.parent = {i+1: i+1 for i in range(n)}
        self.size = {i+1: 1 for i in range(n)}
        
        self.num_of_components = n
        
    def find(self, p):
        
        root = p
        while(root != self.parent[root]):
            root = self.parent[root]
            
        node = p
        while (node != self.parent[node]):
            parent = self.parent[node]
            self.parent[node] = root
            node = parent
            
        return root
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return False
        
        if self.size[rootP] > self.size[rootQ]:
            self.size[rootP] += self.size[rootQ]
            self.parent[rootQ] = rootP
        else:
            self.size[rootQ] += self.size[rootP]
            self.parent[rootP] = rootQ
        
        self.num_of_components -= 1
        return True
