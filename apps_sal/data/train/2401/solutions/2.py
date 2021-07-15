class Solution:
     def wordPattern(self, pattern, str):
         """
         :type pattern: str
         :type str: str
         :rtype: bool
         """
         return list(map(pattern.find, pattern)) == list(map(str.split().index, str.split()))
