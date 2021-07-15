class DSU:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        self.roots[self.find(x)] = self.find(y)
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        m = len(edges)
        edges = sorted(edges, key=lambda x: -x[0])
        type3_exist = set()
        removed = set()
        for i in range(len(edges)):
            typ, n1, n2 = edges[i]
            if (n1, n2) in type3_exist:
                removed.add(i)
                continue
                
            if typ == 3:
                type3_exist.add((n1, n2))
        
        edges = [edge for idx, edge in enumerate(edges) if idx not in removed]
        
        dsu_alice = DSU(n)
        dsu_bob = DSU(n)
        
        count = 0
        for edge in edges:
            typ, n1, n2 = edge
            if typ == 1:
                if dsu_alice.find(n1-1) != dsu_alice.find(n2-1):
                    count += 1
                    dsu_alice.union(n1-1, n2-1)
            if typ == 2:
                if dsu_bob.find(n1-1) != dsu_bob.find(n2-1):
                    count += 1
                    dsu_bob.union(n1-1, n2-1)
            if typ == 3:
                if dsu_bob.find(n1-1) != dsu_bob.find(n2-1) or dsu_alice.find(n1-1) != dsu_alice.find(n2-1):
                    count += 1
                    dsu_alice.union(n1-1, n2-1)
                    dsu_bob.union(n1-1, n2-1)
        
        if len(set([dsu_bob.find(i) for i in range(n)])) != 1 or len(set([dsu_alice.find(i) for i in range(n)])) != 1:
            return -1
        
        return m - count
