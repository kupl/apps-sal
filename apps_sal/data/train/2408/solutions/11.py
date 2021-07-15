class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         chars=set(s)
         return min([s.index(char) for char in chars if s.count(char)==1] or [-1])
