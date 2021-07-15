class Solution:
     def detectCapitalUse(self, word):
         
         return word[1:].islower() or word.isupper() or word.islower()
     
     
     
         """old
         if word[0].isupper():
             if len(word)==1:return True
             if word[1].isupper():
                 for i in range(2,len(word)):
                     if word[i].islower():return False
                 return True                    
             for i in range(2,len(word)):
                 if word[i].isupper():return False
             return True
         for i in range(1,len(word)):
             if word[i].isupper():return False
         return True
         """
         
         """
         :type word: str
         :rtype: bool
         """

