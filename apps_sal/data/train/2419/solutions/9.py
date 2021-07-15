class Solution:
     def repeatedStringMatch(self, a, b):
         """
         :type A: str
         :type B: str
         :rtype: int
         """
         if a is None or len(a) ==0 or b is None or len(b) == 0:
             return -1
         if a == b:
             return 1
         kmp = [0 for _ in range(len(b)+1)]
         j = 0
         for i in range(1, len(b)):
             if b[j] == b[i]:
                 j += 1
                 kmp[i] = j
             else:
                 if j == 0:
                     i += 1
                 else:
                     j = kmp[j-1]
         j = 0
         for i in range(len(a)):
             while j < len(b) and a[(i+j)%len(a)] == b[j]:
                 j += 1
             if j == len(b):
                 return -(-(i+j)//len(a))
             j = kmp[j-1]
         return -1
