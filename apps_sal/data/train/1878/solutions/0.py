class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         res = 0
         temp = sorted(arr)
         sum1, sum2 = 0, 0
         for i in range(0,len(arr)):
             sum1 += arr[i]
             sum2 += temp[i]
             if(sum1 == sum2):
                 res += 1
         return res

