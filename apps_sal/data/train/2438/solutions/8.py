class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        while l:
            if l[-1]:
                return len(l[-1])
            else:
                l.pop(-1)
        return 0
