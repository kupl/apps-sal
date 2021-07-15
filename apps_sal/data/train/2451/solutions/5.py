class Solution:
     def canConstruct(self, ransomNote, magazine):
         """
         :type ransomNote: str
         :type magazine: str
         :rtype: bool
         """
         available_letters = dict()
         
         for c in magazine:
             if c in list(available_letters.keys()):
                 available_letters[c] += 1
             else:
                 available_letters[c] = 1
         
         for c in ransomNote:
             if c not in list(available_letters.keys()):
                 return False
             else:
                 available_letters[c] -= 1
                 if available_letters[c] == 0:
                     del available_letters[c]
         
         return True

