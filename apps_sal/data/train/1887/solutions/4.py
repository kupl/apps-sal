class Solution:
     def findCircleNum(self, M):
         """
         :type M: List[List[int]]
         :rtype: int
         """
         N = len(M)
         seen = set()
         
         def dfs(i):
             for j, flag in enumerate(M[i]):
                 if flag and j not in seen:
                     seen.add(j)
                     dfs(j)
                     
         ans = 0
         for i in range(N):
             if i not in seen:
                 dfs(i)
                 ans += 1
         return ans
