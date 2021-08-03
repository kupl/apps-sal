class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        charMap = {}
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        for char in t:
            if char in charMap and charMap[char] > 0:
                charMap[char] -= 1
            else:
                return False
        return True
