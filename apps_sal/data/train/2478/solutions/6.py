class Solution:

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_map = {}
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
        for char in t_map:
            if char not in s_map or t_map[char] > s_map[char]:
                return char
