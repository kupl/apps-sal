class Solution:
     def isValid(self, s):
         """
         :type s: str
         :rtype: bool
         """
         lefty = ['(', '{', '[']
         D = { ')':'(', '}':'{', ']':'[' }
         L = []
         for b in s:
             if b in lefty:
                 L.append(b)
             else:
                 if len(L)==0 or D[b]!=L.pop():
                     return False
         if len(L)!=0:
             return False
         else:
             return True

