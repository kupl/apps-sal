class Solution:

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ''
        words.sort(key=lambda x: (len(x), x))
        memo = set()
        maxlen = 0
        maxword = ''
        for word in words:
            if len(word) <= 1:
                memo.add(word)
                maxlen = 1
                if maxword == '':
                    maxword = word
            elif word[:-1] in memo:
                memo.add(word)
                if len(word) > maxlen:
                    maxlen = len(word)
                    maxword = word
        return maxword
