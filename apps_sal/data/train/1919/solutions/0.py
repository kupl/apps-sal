class Solution:
     def findOrder(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: List[int]
         """
         n = numCourses  
         graph = {}
         for post, pre in prerequisites:
             if pre in graph:
                 graph[pre].append(post)
             else:
                 graph[pre] = [post]
         
         WHITE = 0 # never explored. NOT CHECKED
         GREY = 1 # in the stack, exploring. CHECKING
         BLACK = 2 # finished explored and we know for a fact there's no loop originated from this. CHECKED
         state = [WHITE for _ in range(0, n)]
         
         res = []
         
         def dfs(i):
             state[i] = GREY
             for child in graph.get(i, []):
                 if state[child] == GREY:
                     return False
                 elif state[child] == WHITE:
                     if not dfs(child):
                         return False
             state[i] = BLACK
             res.insert(0, i)
             return True
         
         for i in range(0, n):
             if state[i] != BLACK:
                 if not dfs(i):
                     return []
         return res

