class Solution:
     def _longestCommonPrefix(self, left, right):
         prefix = ''
         i = j = 0
         while(i < len(left) and j < len(right)):
             if left[i] == right[j]:
                 prefix += left[i]
             else:
                 break
             i += 1
             j += 1
         return prefix
     
     def longestCommonPrefix(self, strs):
         """
         :type strs: List[str]
         :rtype: str
         """
         if not strs:
           return ''
         elif len(strs) == 1:
           return strs[0]
         mid = len(strs)//2
         left, right = self.longestCommonPrefix(strs[mid:]), self.longestCommonPrefix(strs[:mid])
         return self._longestCommonPrefix(left, right)

