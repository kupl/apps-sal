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
        res = list(s)
        while left < right:
            while left < right and res[left] not in vowels:
                left += 1
            while right > left and res[right] not in vowels:
                right -= 1
            (res[left], res[right]) = (res[right], res[left])
            left += 1
            right -= 1
        return ''.join(res)
