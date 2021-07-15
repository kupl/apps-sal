class Solution(object):
     def wordPattern(self, pattern, str):
         """
         :type pattern: str
         :type str: str
         :rtype: bool
         """
         ptMap = {}
         good = True
         wList = str.split(' ')
         if len(wList) != len(pattern):
             good = False
         else:
             for k, v in enumerate(wList):
                 if v in ptMap:
                     if ptMap[v] != pattern[k]:
                         good = False
                 else:
                     if pattern[k] in ptMap.values():
                         good = False
                     else:
                         ptMap[v] = pattern[k]
 
         return good
