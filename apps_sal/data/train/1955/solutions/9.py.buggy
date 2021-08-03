class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(s) < 2 or len(pairs) == 0:
            return s
        
        class UnionFind:
            def __init__(self, N):
                self.arr = [i for i in range(N)]
                
            def find(self, x):
                if self.arr[x] == x:
                    return x
                else:
                    self.arr[x] = self.find(self.arr[x])
                    return self.arr[x]
            
            def union(self, x1, x2):
                self.arr[self.find(x1)] = self.find(x2)
            
        uf = UnionFind(len(s))
        for pair in pairs:
            uf.union(pair[0], pair[1])
        
        g = defaultdict(list)
        for i in range(len(s)):
            g[uf.find(i)].append(s[i])
            
        for k in g:
            g[k].sort(reverse=True)
        
        res = []
        for i in range(len(s)):
            res.append(g[uf.find(i)].pop())
        
        return \"\".join(res)
