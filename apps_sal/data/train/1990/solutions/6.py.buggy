import operator
 class Solution:
     def findLongestChain(self, pairs):
         """
         :type pairs: List[List[int]]
         :rtype: int
         """
         pairs.sort(key=operator.itemgetter(1, 0))
         maxNum = -float('inf')
         ret = 0
         for pair in pairs:
             if pair[0] > maxNum:
                 maxNum = pair[1]
                 ret += 1
         return ret
