class Solution:
     def intersectionSizeTwo(self, intervals):
         res = 0
         last2 = [-float('inf')] * 2
         intervals = sorted(intervals, key=lambda x: x[1])
         for lo, hi in intervals:
             n = sum(x < lo for x in last2)
             res += n
             if n == 2:
                 last2 = hi - 1, hi
             elif n == 1:
                 last2 = last2[1], hi
         return res

