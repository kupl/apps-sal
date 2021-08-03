from collections import defaultdict
 
 class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         
         graph = defaultdict(list)
         for from_, to_ in tickets:
             graph[from_].append(to_)
         
         for each in graph:
             graph[each].sort()
         
         res = []
         self.dfs(graph, "JFK", res)
         return res[::-1]
     
     
     def dfs(self, graph, from_, results):
         
         while graph[from_]:
             curr = graph[from_].pop(0)
             self.dfs(graph, curr, results)
         
         results.append(from_)
