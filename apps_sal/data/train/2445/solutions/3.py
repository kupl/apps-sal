class Solution:
    def detectCapitalUse(self, word):
        return word[1:] == word[1:].lower() or word == word.upper()
