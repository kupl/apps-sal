class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordSet = set(words)

        words.sort(key=lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordSet for k in range(1, len(word))):
                return word
        return ""
