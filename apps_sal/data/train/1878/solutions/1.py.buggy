import collections
 class Solution:
     '''
     >>> sol = Solution()
     >>> sol.maxChunksToSorted([2,1,3,4,4])
     4
     >>> sol.maxChunksToSorted([4, 3, 2, 1, 0])
     1
     >>> sol.maxChunksToSorted([0, 1])
     2
     '''
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         counter = collections.Counter()
         arrtup = []
         for num in arr:
             counter[num] += 1
             arrtup.append((num, counter[num]))
         arrsorted = sorted(arrtup)
         ans, maxnum = 0, (0, 0)
         for x, y in zip(arrtup, arrsorted):
             maxnum = max(maxnum, x)
             if maxnum == y:
                 ans += 1
 
         return ans
 

