class UnionFindSet:
    def __init__(self, n):
        self.p, self.c = [i for i in range(n)], [1] * n
    
    def find(self, v):
        if self.p[v] != v: self.p[v] = self.find(self.p[v])
        return self.p[v]
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2: return False
        if self.c[p1] < self.c[p2]: p1, p2 = p2, p1
        self.p[p2] = p1
        self.c[p1] += self.c[p2]
        return True
    
    def count(self, v):
        return self.c[self.find(v)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ret = 0
        ufs1, ufs2 = UnionFindSet(n + 1), UnionFindSet(n + 1)
        for t, u, v in edges:
            if t == 3:
                f = False
                if ufs1.union(u, v): f = True
                if ufs2.union(u, v): f = True
                if f: ret += 1
        for t, u, v in edges:
            if t == 1 and ufs1.union(u, v): ret += 1
            if t == 2 and ufs2.union(u, v): ret += 1
        if ufs1.count(1) != n or ufs2.count(1) != n: return -1
        return len(edges) - ret
