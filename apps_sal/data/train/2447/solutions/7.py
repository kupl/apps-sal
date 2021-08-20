class Solution:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s = list(s)
        l = len(s)
        (p1, p2) = (0, l - 1)
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                (s[p1], s[p2]) = (s[p2], s[p1])
                p1 += 1
                p2 -= 1
            elif s[p1] not in vowels:
                p1 += 1
            elif s[p2] not in vowels:
                p2 -= 1
        return ''.join(s)
