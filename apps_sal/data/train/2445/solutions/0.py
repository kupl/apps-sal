class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        elif word.isupper() or word.islower():
            return True
        elif len(word) > 1:
            return word.istitle()
        else:
            return False
