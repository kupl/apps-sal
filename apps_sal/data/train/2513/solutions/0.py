class Solution:
     def findNthDigit(self, n):
         """
         :type n: int
         :rtype: int
         """
         i=count=9
         while count < n:
             i *= 10
             count += i * len(str(i))
         div, mod = divmod(n-(count-i*len(str(i))), len(str(i)))
         print(i, count, div, mod)
         target = (i//9-1) + div
         if mod == 0:
             print(target, int(str(target)[-1]))
             return int(str(target)[-1])
         else:
             return int(str(target+1)[mod-1])
