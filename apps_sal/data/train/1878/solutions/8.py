class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         
         sarr = sorted(arr)
         table = {}
         for i, n in enumerate(sarr):
             if n not in table:
                 table[n] = [i, i]
             else:
                 table[n][1] += 1
         
         c = -1
         chunks = 0
         for i, n in enumerate(arr):
             c = max(c, table[n][0])
             if table[n][0] < table[n][1]:
                 table[n][0] += 1
             if c == i:
                 chunks += 1
         return chunks
