from heapq import *
 class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         import collections
         targets=collections.defaultdict(list)
         for a,b in sorted(tickets):
             targets[a]+=b,
         # for key in targets:
         #     heapify(targets[key])
         res=[]
         self.visit('JFK',res, targets)
         return res[::-1]
     
     def visit(self,airport, res, targets):
         while targets[airport]:
             self.visit(targets[airport].pop(0),res,targets)
         res.append(airport)
