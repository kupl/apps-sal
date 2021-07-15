class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        amy = UnionFind(n)
        bob = UnionFind(n)
        edges.sort(key=lambda x: x[0], reverse=True)
        added = 0
        for e in edges:
            t = e[0]
            s = e[1]
            des = e[2]
            if t == 3:
                a = amy.union(s-1, des-1)
                b = bob.union(s-1, des-1)
                if a or b:
                    added += 1
            elif t == 1:
                if amy.union(s-1, des-1):
                    added += 1
            elif t == 2:
                if bob.union(s-1, des-1):
                    added += 1
        if amy.united() and bob.united():
            return len(edges) - added
        return -1
        
        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.distinct = n
    
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
            self.rank[pb] += 1
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        self.distinct -= 1
        return True

    def united(self):
        return self.distinct == 1

