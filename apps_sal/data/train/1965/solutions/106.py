class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.size = 1
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1
        self.size += 1
        return True
    
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2, ans = UnionFindSet(n), UnionFindSet(n), 0
\t\t
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                ans += 1
        
        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                ans += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                ans += 1
   
        return ans if uf1.size == n and uf2.size == n else -1
# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         self.father_alice = [i for i in range(n + 1)]
#         self.father_bob = [i for i in range(n + 1)]
#         res = 0
#         edge_alice, edge_bob = 0, 0
#         for type, u, v in edges:
#             if type == 3:
#                 if self.connect(u, v, True) == 1:
#                     edge_alice += 1
#                     edge_bob += 1
#                 else:
#                     res += 1
                
#                 self.connect(u, v, False)
        
#         for type, u, v in edges:
#             if type == 1:
#                 if self.connect(u, v, True) == 1:
#                     edge_alice += 1
#                 else:
#                     res += 1
#             elif type == 2:
#                 if self.connect(u, v, False) == 1:
#                     edge_bob += 1
#                 else:
#                     res += 1
        
#         if edge_alice == edge_bob == n - 1:
#             return res
#         return -1
    
    
    
#     def find(self, x, is_alice):
#         if is_alice:
#             if self.father_alice[x] == x:
#                 return self.father_alice[x]
#             self.father_alice[x] = self.find(self.father_alice[x], True)
#             return self.father_alice[x]
#         else:
#             if self.father_bob[x] == x:
#                 return self.father_bob[x]
#             self.father_bob[x] = self.find(self.father_bob[x], False)
#             return self.father_bob[x]
    
#     def connect(self, a, b, is_alice):
#         if is_alice:
#             root_a = self.find(a, True)
#             root_b = self.find(b, True)
#             if root_a == root_b:
#                 return 0
#             else:
#                 self.father_alice[max(root_a, root_b)] = min(root_a, root_b)
#                 return 1
#         else:
#             root_a = self.find(a, False)
#             root_b = self.find(b, False)
#             if root_a == root_b:
#                 return 0
#             else:
#                 self.father_bob[max(root_a, root_b)] = min(root_a, root_b)
#                 return 1
        
        
        
        
        
#         self.father_alice = [i for i in range(n + 1)]
#         self.father_bob = [i for i in range(n + 1)]
        
#         res = 0
#         for type, u, v in edges:
#             if type == 3:
#                 res += self.connect(u, v, True)
#                 self.connect(u, v, False)
        
#         for type, u, v in edges:
#             if type == 1:
#                 res += self.connect(u, v, True)
#             elif type == 2:
#                 res += self.connect(u, v, False)
        
        
#         if self.check_valid(True) and self.check_valid(False):
#             return res
#         return -1
    
    
#     def find(self, x, is_alice):
#         if is_alice:
#             if self.father_alice[x] == x:
#                 return self.father_alice[x]
#             self.father_alice[x] = self.find(self.father_alice[x], True)
#             return self.father_alice[x]
        
#         else:
#             if self.father_bob[x] == x:
#                 return self.father_bob[x]
#             self.father_bob[x] = self.find(self.father_bob[x], False)
#             return self.father_bob[x]
        
#     def connect(self, a, b, is_alice):
#         if is_alice:
#             root_a = self.find(a, True)
#             root_b = self.find(b, True)
#             if root_a != root_b:
#                 self.father_alice[max(root_a, root_b)] = min(root_a, root_b)
#                 return 0
#             return 1
        
#         else:
#             root_a = self.find(a, False)
#             root_b = self.find(b, False)
#             if root_a != root_b:
#                 self.father_bob[max(root_a, root_b)] = min(root_a, root_b)
#                 return 0
#             return 1
        
#     def check_valid(self, is_alice):
#         if is_alice:
#             root = self.find(1, True)
#             for i in range(1, len(self.father_alice)):
#                 if self.find(i, True) != root:
#                     return False
#             return True
        
#         else:
#             root = self.find(1, False)
#             for i in range(1, len(self.father_bob)):
#                 if self.find(i, False) != root:
#                     return False
#             return True
