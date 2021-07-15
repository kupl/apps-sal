class Solution:
     def reachNumber(self, target):
         target = abs(target)
         def binary_search(lo, hi):
             if lo >= hi:
                 return lo
 
             mi = lo + (hi - lo) // 2
             t = mi * (mi + 1) // 2
 
             if t == target:
                 return mi
             elif t < target:
                 return binary_search(mi + 1, hi)
             else:
                 return binary_search(lo, mi)
 
         res = binary_search(0, target)
         if target % 2 == 0 and 1 <= res % 4 <= 2:
             return res + 3 - res % 4
         elif target % 2 == 1 and (res % 4 == 3 or res % 4 == 0):
             return res + 4 - (res - 1) % 4
         else:
             return res
