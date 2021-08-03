class UnionFind:
    def __init__(self, items):
        self.leader = {}
        for item in items:
            self.leader[item] = item
    
    def union(self, i1, i2):
        l1, l2 = self.find(i1), self.find(i2)
        if l1 == l2:
            return False
        self.leader[l1] = self.leader[l2]
        return True
        
    def find(self, i):
        if self.leader[i] != i:
            self.leader[i] = self.find(self.leader[i])
        return self.leader[i]
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        \"\"\"
        Check if A and B can traverse the entire graph at first
        \"\"\"
        items = [i for i in range(1, n + 1)]
        uf1 = UnionFind(items)
        uf2 = UnionFind(items)
        
        a_essential_edges = 0
        b_essential_edges = 0
        removable_edges = 0
        
        for [t, u, v] in edges:
            if t == 3:
                union_success = uf1.union(u, v)
                uf2.union(u, v)
                
                if union_success:
                    a_essential_edges += 1
                    b_essential_edges += 1
                else:
                    removable_edges += 1
                    
        for [t, u, v] in edges:
            if t == 1:
                union_success = uf1.union(u, v)
                if union_success:
                    a_essential_edges += 1
                else:
                    removable_edges += 1
        for [t, u, v] in edges:
            if t == 2:
                union_success = uf2.union(u, v)
                if union_success:
                    b_essential_edges += 1
                else:
                    removable_edges += 1
        
        
        
        return removable_edges if a_essential_edges == b_essential_edges == n - 1 else -1
        
