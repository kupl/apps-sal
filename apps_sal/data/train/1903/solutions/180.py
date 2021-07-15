# # Kruskal
# # O(n ^ 2)
# class UnionFindSet:
#     def __init__(self, n):
#         self.parents = [i for i in range(n + 1)]
#         self.ranks = [0 for i in range(n + 1)]
        
#     def find(self, u):
#         if u != self.parents[u]:
#             self.parents[u] = self.find(self.parents[u])            
#         return self.parents[u]
    
#     def union(self, u, v):
#         pu = self.find(u)
#         pv = self.find(v)
#         if pu == pv: return False
        
#         if self.ranks[pu] < self.ranks[pv]:
#             self.parents[pu] = pv
#         elif self.ranks[pu] > self.ranks[pv]:
#             self.parents[pv] = pu
#         else:
#             self.parents[pu] = pv
#             self.ranks[pv] += 1
            
#         return True


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         edges = []
#         for i in range(n):
#             for j in range(i + 1, n):
#                 edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
#         edges.sort()
#         ans = 0
#         count = 0
#         uf = UnionFindSet(n)
#         for e in edges:
#             if not uf.union(e[1], e[2]): continue
#             ans += e[0]
#             count += 1
#             if count == n - 1: return ans
            
#         return ans
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        ds = [float('inf') for _ in range(n)]
        for i in range(1, n):
            ds[i] = dist(points[0], points[i])
        
        ans = 0
        for i in range(1, n):
            v = ds.index(min(ds))
            ans += ds[v]
            ds[v] = float('inf')
            for i in range(n):
                if ds[i] == float('inf'): continue
                ds[i] = min(ds[i], dist(points[i], points[v]))
                
        return ans
