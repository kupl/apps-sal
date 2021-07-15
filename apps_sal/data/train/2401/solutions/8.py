class Solution:
     def wordPattern(self, pattern, str):
         """
         :type pattern: str
         :type str: str
         :rtype: bool
         """
         if pattern is None or str is None:
             return False
         
         dic_p2w = {}
         pset = set()
         words = str.split(' ')
         if len(pattern) != len(words):
             return False
         
         for i in range(len(words)):
             pset.add(pattern[i])
             if pattern[i] not in dic_p2w:
                 dic_p2w[pattern[i]] = words[i]
             else:
                 if dic_p2w[pattern[i]] != words[i]:
                     return False
         return len(pset) == len(set(words)) 
