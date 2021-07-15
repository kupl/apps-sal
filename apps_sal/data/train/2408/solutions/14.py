class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         s_set = set()
         for index, char in enumerate(s):
             if char in s_set:
                 continue
             s_set.add(char)
             if s.count(char) == 1:
                 return index
         return -1

