class Solution:
    def lengthOfLastWord(self, s):
        res = 0
        last = 0
        for i in s:
            if(i == ' '):
                res = 0
            else:
                res += 1
                last = res

        return last
        """
         :type s: str
         :rtype: int
         """
