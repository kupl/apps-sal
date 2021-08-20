class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        longest = 0
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for (key, val) in counter.items():
            if val % 2 == 0:
                longest += val
            else:
                longest += val - 1
        if longest < len(s):
            longest += 1
        return longest
