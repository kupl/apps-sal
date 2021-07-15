class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         cnt = 0
         max_curr = -1
         for i in range(len(arr)):
             max_curr = max(max_curr, arr[i])
             if max_curr == i:
                 cnt += 1
         return cnt
