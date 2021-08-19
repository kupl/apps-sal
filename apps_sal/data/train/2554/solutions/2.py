class Solution:

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words_set = set([''])
        longest = ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest
