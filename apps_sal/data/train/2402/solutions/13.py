class Solution:

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        result = list()
        for word in words:
            new_word = ''.join(reversed(list(word)))
            result.append(new_word)
        return ' '.join(result)
