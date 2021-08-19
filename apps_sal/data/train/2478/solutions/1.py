class Solution:

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        t_dict = {}
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1
        result = ''
        for letter in t:
            if letter not in s_dict:
                result = letter
            elif t_dict[letter] > s_dict[letter]:
                result = letter
        return result
