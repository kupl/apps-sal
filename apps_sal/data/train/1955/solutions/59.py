class UnionFind():
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self,A):
        root = A
        
        while root != self.parent[root]:
            root = self.parent[root]
        
        while A!=root:
            old_parent = self.parent[A]
            self.parent[A] = root
            A = old_parent
        return root
    
        
    def union(self,A,B):
        root_A = self.find(A)
        root_B = self.find(B)
        
        if self.size[root_A]>self.size[root_B]:           
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        else:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
            
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        uf = UnionFind(len(s))
        d = collections.defaultdict(list)
        res = []
        
        for i,j in pairs:
            uf.union(i,j)
        
        for i in range(len(s)):
            d[uf.find(i)].append(s[i])
        
        for parent in d:
            d[parent].sort(reverse = True)
        
        for i in range(len(s)):
            res.append(d[uf.find(i)].pop())
            
        return \"\".join(res)
            
        
