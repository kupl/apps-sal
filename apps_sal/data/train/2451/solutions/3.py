class Solution:
     def canConstruct(self, ransomNote, magazine):
         """
         :type ransomNote: str
         :type magazine: str
         :rtype: bool
         """
         for i in set(ransomNote):
             if i not in set(magazine) or ransomNote.count(i)>magazine.count(i):
                 return False
         return True

