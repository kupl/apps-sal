class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         graph = {}
         for line in tickets:
             if line[0] not in graph:
                 graph[line[0]] = [line[1]]
             else:
                 graph[line[0]].append(line[1])
         for key in graph:
             graph[key] = sorted(graph[key], reverse = True)
         
         res = []
         cur = "JFK"
         stack = []
         for i in range(len(tickets)):
             while (cur not in graph) or (not graph[cur]):
                 stack.append(cur)
                 cur = res.pop()   
             res.append(cur)
             cur = graph[cur].pop()
             
         res.append(cur)
         while stack:
             res.append(stack.pop())
         return res
             
             

