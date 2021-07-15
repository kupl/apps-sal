class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         d = collections.defaultdict(list)
         tickets.sort()
         for i,j in tickets:
             d[i] += [j]
             
         def dfs(path, start):
             path += [start]
             if len(path) == length:
                 return True
             i = 0
             while i <len(d[start]):
                 next = d[start].pop(0)
                 print((next, d[start]))
                 i += 1
                 if dfs(path, next):
                     return True
                 d[start] += [next]
             path.pop()
             return False    
                 
         path, length = [], len(tickets) + 1
         dfs(path, 'JFK')
         return path
                 

