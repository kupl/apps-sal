class Solution:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i = 0
        j = len(s) - 1
        while i <= j:
            while s[i] not in yuanyin and i < j:
                i += 1
            while s[j] not in yuanyin and i < j:
                j -= 1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return ''.join(s)
