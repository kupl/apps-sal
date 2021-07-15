class Solution:
     def findCircleNum(self, M):
         """
         :type M: List[List[int]]
         :rtype: int
         """
     # dfs solution
     #     seen = set()
     #     rtn = 0
     #     for i in range(len(M)):
     #         if i not in seen:
     #             rtn += 1
     #             self.dfs(i, M, seen)
     #     return rtn
     # def dfs(self,i,M,seen):
     #     for nei,adj in enumerate(M[i]):
     #         if adj and nei not in seen:
     #             seen.add(nei)
     #             self.dfs(nei, M, seen)
     
         # union find solution
         ds = DisjointSet()
         for i in range(len(M)):
             ds.make_set(i)
         for i in range(len(M)):
             for j in range(i,len(M)):
                 if M[i][j]==1:
                     ds.union(i,j)
         return ds.num_sets
 
 class Node:
     def __init__(self,data):
         self.data=data
         self.parent=self
         self.rank=0
 class DisjointSet:
     def __init__(self):
         self.map={}
         self.num_sets=0
     def make_set(self,i):
         node = Node(i)
         self.map[i]=node
         self.num_sets+=1
     def union(self,i,j):
         node1 = self.map[i]
         node2 = self.map[j]
         parent1 = self.find_set(node1)
         parent2 = self.find_set(node2)
         if parent1 == parent2:
             return
         if parent1.rank >= parent2.rank:
             if parent1.rank==parent2.rank:
                 parent1.rank+=1
             parent2.parent=parent1
         else:
             parent1.parent = parent2
         self.num_sets-=1
     def find_set(self,node):
         if node.parent==node:
             return node
         node.parent = self.find_set(node.parent)
         return node.parent
         
