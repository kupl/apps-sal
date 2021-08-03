class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for c in s:
        #     if s.count(c)==1:
        #         return s.find(c)
        # return -1

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
