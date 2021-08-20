class Solution:

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.upper() or word == word.lower() or word == word[0].upper() + word[1:].lower()
