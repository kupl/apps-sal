import queue
 
 class Solution:
     def findOrder(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: List[int]
         """
         graph = {}
         for course, prereq in prerequisites:
             graph[prereq] = graph[prereq] + [course] if prereq in graph else [course]
         degree = [0] * numCourses
         for course, _ in prerequisites:
             degree[course] += 1
         q = queue.Queue()
         for i in range(numCourses):
             if degree[i] == 0:
                 q.put(i)
         res = []
         while not q.empty():
             pre = q.get()
             if pre in graph:
                 for course in graph[pre]:
                     degree[course] -= 1
                     if degree[course] == 0:
                         q.put(course)
             res.append(pre)
         return res if len(res) == numCourses else []
