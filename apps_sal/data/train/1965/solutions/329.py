class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key=lambda l:l[0], reverse=True)
        uf_a = [i for i in range(n)]
        uf_b = [j for j in range(n)]
        
        cnt = 0        
        for edge in edges:
            if edge[0] == 3:
                cnt += self.union(uf_a, edge[1]-1, edge[2]-1)
                self.union(uf_b, edge[1]-1, edge[2]-1)
            elif edge[0] == 1:
                cnt += self.union(uf_a, edge[1]-1, edge[2]-1)
            else: # edge[0] == 2
                cnt += self.union(uf_b, edge[1]-1, edge[2]-1)
        if not self.connected(uf_a) or not self.connected(uf_b):
            return -1
        return len(edges)-cnt
    
    def connected(self, uf: List[int]) -> bool:
        r = self.root(uf, 0)
        for i in range(1, len(uf)):
            if self.root(uf, i) != r:
                return False
        return True
                
    def root(self, uf: List[int], a: int) -> int:
        cur = a
        while uf[cur] != cur:
            cur = uf[cur]
        root = cur
        while uf[a] != root:
            parent = uf[a]
            uf[a] = root
            a = parent
        return root
    
    def union(self, uf: List[int], a: int, b: int) -> int:
        root_a = self.root(uf, a)
        root_b = self.root(uf, b)
        if root_a == root_b:
            return 0
        small = min(root_a, root_b)
        large = max(root_a, root_b)
        uf[large] = small
        return 1

