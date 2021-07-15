from collections import defaultdict
 
 NOT_VISITED, VISITING, VISITED = 'NOT_VISITED', 'VISITING', 'VISITED'
 
 
 class Solution:
     def findOrder(self, numCourses, prerequisites):
         al = {i: [] for i in range(numCourses)}
         for cn, pn in prerequisites:
             al[cn].append(pn)
         vst = defaultdict(lambda: NOT_VISITED)
         srt = []
 
         def dfs(cn):
             '''
             Adds to topo sort if no cycle found
             '''
             if vst[cn] == VISITING:
                 return False
             elif vst[cn] == VISITED:
                 return True
 
             vst[cn] = VISITING
 
             for pre in al[cn]:
                 if not dfs(pre):
                     return False  # cycle found, no such topo sort
 
             vst[cn] = VISITED
             srt.append(cn)
 
             return True
 
         for cn in range(numCourses):
             if not dfs(cn):
                 return []  # cycle found, no such topo sort
 
         return srt

