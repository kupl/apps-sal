from collections import deque, defaultdict
 import heapq
 
 class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         edges = defaultdict(list)
         for ticket in tickets:
             heapq.heappush(edges[ticket[0]], ticket[1])
         order = deque([])
         self.dfs(order, edges, 'JFK')
         return list(order)
     
     def dfs(self, order, edges, city):
         while edges[city]:
             next_city = heapq.heappop(edges[city])
             self.dfs(order, edges, next_city)
         order.appendleft(city)
         
