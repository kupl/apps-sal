class Solution:
     def findOrder(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: List[int]
         """
         graph=[[]for _ in range(numCourses)]
         degree=[0 for _ in range(numCourses)]
         
         for f,i  in prerequisites:
             degree[f]+=1
             graph[i].append(f)
         res=[]
         print(degree)
         now_can_learn=[j for j in range(numCourses) if degree[j] == 0]
         while (len(now_can_learn)>0):
             curr=now_can_learn.pop()
             res.append(curr)
             for j in graph[curr]:
                 degree[j] -=1
                 if degree[j]==0:
                     now_can_learn.append(j)
         return res if len(res)==numCourses else []
         
         
                         

