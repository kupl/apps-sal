class Solution:
     def findLongestChain(self, pairs):
         """
         :type pairs: List[List[int]]
         :rtype: int
         """
         if not pairs:
             return 0
         
         pairs.sort(key= lambda x: x[1])        
         size = 1
         prev = pairs[0]
         
         for p in pairs[1:]:
             if prev[1] < p[0]:
                 size += 1
                 prev = p
         return size
