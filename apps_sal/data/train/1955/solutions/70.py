from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         def find(uf, node):        
#             if uf[node] != node:
#                 return find(uf, uf[node])
                
#             return node
            
#         def union(uf, node1, node2):
#             uf[find(uf, node1)] = find(uf, node2)
            
#         uf = list(range(len(s)))
        
#         if not pairs:
#             return s
        
#         for pair in pairs:
#             union(uf, pair[0], pair[1])
        
#         groups = defaultdict(list)
        
#         for i in range(len(s)):
#             groups[find(uf, i)].append(s[i])
                        
#         for group in groups:
#             groups[group].sort(reverse=True)
        
#         res = []

#         for i in range(len(s)):
#             res.append(groups[find(uf, i)].pop())
            
#         return ''.join(res)
    
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

