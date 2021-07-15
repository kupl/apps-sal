class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges_alice = [e for e in edges if e[0] == 1 or e[0] == 3]
        edges_bob = [e for e in edges if e[0] == 2 or e[0] == 3]
        edges_both = [e for e in edges if e[0] == 3]
        
        nodes = [i for i in range(1, n + 1)]
        
        union_find = unionFind(nodes)
        for edge in edges_alice:
            union_find.union(edge[1], edge[2])
        if union_find.count != 1:
            return -1
        num_removed_edge_alice = len(edges_alice) - (n - 1)
        
        union_find = unionFind(nodes)
        for edge in edges_bob:
            union_find.union(edge[1], edge[2])
        if union_find.count != 1:
            return -1
        num_removed_edge_bob = len(edges_bob) - (n - 1)
        
        union_find = unionFind(nodes)
        for edge in edges_both:
            union_find.union(edge[1], edge[2])
        num_removed_edge_both = len(edges_both) - (n - union_find.count)
        
        return num_removed_edge_alice + num_removed_edge_bob - num_removed_edge_both
        

class unionFind:
    def __init__(self, nodes):
        self.father = {node: node for node in nodes}
        self.count = len(nodes)
        
    def find(self, node):
        if self.father[node] == node:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]
    
    def union(self, node_a, node_b):
        father_a = self.find(node_a)
        father_b = self.find(node_b)
        if father_a != father_b:
            self.father[father_a] = father_b
            self.count -= 1
            

