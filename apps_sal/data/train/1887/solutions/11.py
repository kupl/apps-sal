class UnionFind(object):
     def __init__(self, n):
         self.__parent = dict()
         self.__circles = n
         for i in range(n):
             self.__parent[i] = i
         
     @property
     def parent(self):
         return self.__parent
     
     @parent.setter
     def parent(self, key, value):
         self.__parent[key] = val
     
     @property
     def circles(self):
         return self.__circles
     
     def circles_decrement(self):
         self.__circles -= 1
         
         
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
             self.circles_decrement()
         
 
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
         
