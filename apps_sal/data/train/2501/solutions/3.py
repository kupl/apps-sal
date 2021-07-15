class Solution:
     def reverseStr(self, s, k):
         """
         :type s: str
         :type k: int
         :rtype: str
         """
         n = len(s)
         p = 0
         
         s = list(s)
         
         while True:
             if p >= n:
                 break
             p1 = p + k
             if p1>n:
                 p1 = n
             p0 = p
             while p0 < p1:
                 p1-=1
                 s[p0], s[p1] = s[p1],s[p0]
                 p0+=1
             p += k*2
         return ''.join(s)

