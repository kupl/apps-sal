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

# from collections import defaultdict

# class Solution:
#     def find(self,x):
#         if(x!=self.parent[x]):
#             x=self.find(self.parent[x])
#         return x
        
        
#     def union(self,x,y):
#         x_find=self.find(x)
#         y_find=self.find(y)
#         self.parent[x_find]=y_find
        
    
    
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         n=len(s)
#         self.parent=list(range(n))
        
#         for x,y in pairs:
#             self.union(x,y)
        
#         # print(self.parent)
        
#         groups=defaultdict(list)
#         for i in range(n):
#             tem=self.find(i)
#             # self.parent[i]=tem
#             groups[tem].append(s[i])    
#             # print(tem)
#         # print(self.parent)
        
#         ans=\"\"
#         for comp_id in groups.keys(): 
#             groups[comp_id].sort(reverse=True)
            
#         # print(groups)
        
#         for i in range(n): 
#             ans+=groups[self.find(i)].pop()
#         return ans
        
        
# # #         for i in range(len(s)):
# # #             if(i not in added):
# # #                 groups[i]=[i]
        
# #         # print(groups)
# #         ls=dict()
# #         for i,j in groups.items():
# #             ls[tuple(j)]=sorted([s[ele] for ele in j])
# #         # print(ls)
        
# #         ans=\"\"
# #         for i in range(len(s)):
# #             ans+=ls[tuple(groups[self.parent[i]])].pop(0)
        
# #         return ans
                
        
            
        
        
        
        
# # #         self.ans=s
# # #         visited=set()
# # # #         def traverse(st,pair,i):
# # # #             print(st,i)
# # # #             if(st in visited):
# # #                 return
# # #             visited.add(st)
# # #             a,b=pair[i][0],pair[i][1]
# # #             st=list(st)
# # #             st[a],st[b]=st[b],st[a]
# # #             st=\"\".join(st)
# # #             self.ans=min(self.ans,st)
# # #             # tem=st[:]
# # #             for j in range(len(pair)):
# # #                 if(i!=j):
# # #                     traverse(st,pair,j)
        
        
        
        
# #             # traverse(s,pairs,i)
        
# #         q=[s]
# #         while(q!=[]):
# #             tem=q.pop(0)
# #             if(tem in visited):
# #                 continue
# #             visited.add(tem)
# #             self.ans=min(self.ans,tem)
# #             for i in range(len(pairs)):
# #                 a,b=pairs[i][0],pairs[i][1]
# #                 tem=list(tem)
# #                 tem[a],tem[b]=tem[b],tem[a]
# #                 tem=\"\".join(tem)
# #                 q.append(tem)
            
        
# #         return self.ans

