class Solution:
     def findLongestChain(self, pairs):
         """
         :type pairs: List[List[int]]
         :rtype: int
         """
         cur, res = float('-inf'), 0
         for x, y in sorted(pairs, key=operator.itemgetter(1)):
             if cur < x:
                 cur = y
                 res += 1
         return res

