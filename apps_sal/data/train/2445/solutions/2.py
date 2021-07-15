class Solution:
     def detectCapitalUse(self, word):
         """
         :type word: str
         :rtype: bool
         """
         for i, w in enumerate(word):
             is_cap = ord(w) < ord('a')
             if i == 0:
                 if is_cap:
                     first_cap = True
                     keep_cap = False
                 else:
                     first_cap = False
                     keep_cap = False
             else:
                 if not first_cap and is_cap:
                     return False
                 if keep_cap and not is_cap:
                     return False
                 if not keep_cap and i > 1 and is_cap:
                     return False
                 if i == 1 and is_cap and first_cap:
                     keep_cap = True
         return True
             

