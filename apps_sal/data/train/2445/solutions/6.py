class Solution:

    def detectCapitalUse(self, word):
        return word[1:].islower() or word.isupper() or word.islower()
        'old\n         if word[0].isupper():\n             if len(word)==1:return True\n             if word[1].isupper():\n                 for i in range(2,len(word)):\n                     if word[i].islower():return False\n                 return True                    \n             for i in range(2,len(word)):\n                 if word[i].isupper():return False\n             return True\n         for i in range(1,len(word)):\n             if word[i].isupper():return False\n         return True\n         '
        '\n         :type word: str\n         :rtype: bool\n         '
