class UF:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        
    def union(self, a ,b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[ra] = rb
    
    def find(self, a):
        while a!= self.parent[a]:
            a = self.parent[a]
        return a

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf, res, m = UF(len(s)), [], defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        for comp_id in list(m.keys()): 
            m[comp_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
        
        '''
        cbad
        [[0,3],[1,2],[0,2]]
        
        '''

