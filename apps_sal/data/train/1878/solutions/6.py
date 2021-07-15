class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         stack = []
         for e in reversed(arr):
             min_so_far = e
             while True:
                 if len(stack) == 0 or e <= stack[-1][0]:
                     stack.append([min_so_far, e])
                     break
                 if e > stack[-1][1]:
                     min_so_far = min(min_so_far, stack.pop()[0])
                 else:
                     stack[-1][0] = min(min_so_far, stack[-1][0])
                     break
                     
         return len(stack)
