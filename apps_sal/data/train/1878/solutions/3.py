class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         mxvs, mnvs = [-1] * len(arr), [10**8 + 1] * len(arr)
         for i, v in enumerate(arr):
             if i == 0:
                 mxvs[i] = arr[i]
             else:
                 mxvs[i] = max(mxvs[i-1], v)
         for i in range(len(arr))[::-1]:
             if i == len(arr) - 1:
                 mnvs[i] = arr[i]
             else:
                 mnvs[i] = min(mnvs[i+1], arr[i])
         
         cnt = 0
         for i in range(len(arr)):
             if mxvs[i] <= (mnvs[i+1] if i < len(arr) - 1 else 10**8 + 1):
                 cnt += 1
         return cnt

