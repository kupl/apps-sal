class DisjointSet:
    
    def __init__(self):
        self.parent = dict()
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_a] = root_b
        return True
    
    def find(self, a):
        if a not in self.parent:
            self.parent[a] = a
            return a
        
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ds = DisjointSet()
        
        for u, v in pairs:
            ds.union(u, v)
        
        hashmap = collections.defaultdict(list)
        for i, c in enumerate(s):
            root = ds.find(i)
            hashmap[root].append((c, i))
        
        for root in hashmap:
            hashmap[root].sort(reverse=True)
        
        ans = []
        for i in range(len(s)):
            root = ds.find(i)
            c, _ = hashmap[root].pop()
            ans.append(c)
        return \"\".join(ans)
        
