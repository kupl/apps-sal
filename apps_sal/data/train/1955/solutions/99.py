# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#             class UF:
#                 def __init__(self, n): self.p = list(range(n))
#                 def union(self, x, y): self.p[self.find(x)] = self.find(y)
#                 def find(self, x):
#                     if x != self.p[x]: self.p[x] = self.find(self.p[x])
#                     return self.p[x]
#             uf, res, m = UF(len(s)), [], defaultdict(list)
#             for x,y in pairs: 
#                 uf.union(x,y)
#             for i in range(len(s)): 
#                 m[uf.find(i)].append(s[i])
#             for comp_id in m.keys(): 
#                 m[comp_id].sort(reverse=True)
#             for i in range(len(s)): 
#                 res.append(m[uf.find(i)].pop())
#             return ''.join(res)

from collections import defaultdict

class Solution:
    def find(self,x):
        if(x!=self.parent[x]):
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
        
    def union(self,x,y):
        x_find=self.find(x)
        y_find=self.find(y)
        self.parent[x_find]=y_find
        
    
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        self.parent=list(range(n))
        
        for x,y in pairs:
            self.union(x,y)
        
        # print(self.parent)
        
        groups=defaultdict(list)
        for i in range(n):
            tem=self.find(i)
            # self.parent[i]=tem
            groups[tem].append(s[i])    
            # print(tem)
        # print(self.parent)
        
        ans=[]
        for comp_id in groups.keys(): 
            groups[comp_id].sort(reverse=True)
            
        # print(groups)
        
        for i in range(n): 
            ans.append(groups[self.find(i)].pop())
        return \"\".join(ans)
        
