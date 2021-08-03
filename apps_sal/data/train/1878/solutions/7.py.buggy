import math
 class Solution:
     def maxChunksToSorted(self, arr):
         count = 0
 
         minVal = [0] * len(arr)
         minSofar = math.inf
         for idx in reversed(range(len(arr))):
             minVal[idx] = min(minSofar, arr[idx])
             minSofar = minVal[idx]
 
         maxSofar = -math.inf
         for idx in range(len(arr)):
             maxSofar = max(maxSofar, arr[idx])
             if idx == len(arr) - 1:
                 count += 1
             elif maxSofar <= minVal[idx+1]:
                 count+=1
 
 
         return count
