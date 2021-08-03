class Solution:
    def reverseWords(self, s):
        if len(s) < 2:
            return s

        words = s.split(' ')
        for i, word in enumerate(words):
            l, m = 0, len(word) - 1
            w = list(word)
            while l < m:
                w[l], w[m] = w[m], w[l]
                l += 1
                m -= 1
            words[i] = ''.join(w)
        return ' '.join(words)

        """
         :type s: str
         :rtype: str
         """
