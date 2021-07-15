class UnionFind(object):
     def __init__(self, n):
         self.parent = dict()
         self.circles = n
         for i in range(n):
             self.parent[i] = i
             
     def find(self, s):
         while self.parent[s] != s:
             self.parent[s] = self.parent[self.parent[s]]
             s = self.parent[s]
         return s
     
     def union(self, s1, s2):
         root_s1 = self.find(s1)
         root_s2 = self.find(s2)
         if root_s1 != root_s2:
             self.parent[root_s2] = root_s1
             self.circles -= 1
         
         
 
 class Solution:
     
     def findCircleNum(self, M):
         """
         :type M: List[List[int]]
         :rtype: int
         """
         if M is None or len(M) == 0:
             return 0
         
         n = len(M)
         uf = UnionFind(n)
         
         for i in range(n):
             for j in range(i + 1, n):
                 if M[i][j] == 1:
                     uf.union(i, j)
                     
         return uf.circles
         
