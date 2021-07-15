class Solution:
     def countSegments(self, s):
         """
         :type s: str
         :rtype: int
         """
         '''
         counter = 0
         wasspace = 1
         for char in s:
             if char == " ":
                 wasspace = 1
                 continue
             if wasspace == 1:
                 counter += 1
                 wasspace = 0
         return counter
         '''
         return len(s.split())
