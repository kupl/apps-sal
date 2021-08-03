class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dic = {}
        # for item in s:
        #     if item not in dic:
        #         dic[item] = 1
        #     else:
        #         dic[item] += 1
        # for i in t:
        #     if i not in dic:
        #         return False
        #     else:
        #         dic[i] -= 1
        # return all(value == 0 for value in dic.values())

        # fastest way till now with reference to the others' submissions
        if len(s) != len(t):
            return False
        if s == t:
            return True
        for i in map(chr, range(97, 123)):
            if s.count(i) != t.count(i):
                return False
        return True
