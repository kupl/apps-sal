class Solution:
     def canConstruct(self, ransomNote, magazine):
         a = set(ransomNote)
         b = set(magazine)
         for element in a:
             if ransomNote.count(element) > magazine.count(element):
                 return False
         return True
