class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         wholeletter = 'qwertyuioplkjhgfdsazxcvbnm'
         newindex = [s.index(x) for x in wholeletter if s.count(x) == 1]
         return min(newindex) if len(newindex) >0 else -1
         

