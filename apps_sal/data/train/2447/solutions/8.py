class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        res = [s[0]] * len(s)
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                res[left], res[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in vowels:
                    res[left] = s[left]
                    left += 1
                if s[right] not in vowels:
                    res[right] = s[right]
                    right -= 1
        if left == right:
            res[left] = s[left]
        return ''.join(res)
