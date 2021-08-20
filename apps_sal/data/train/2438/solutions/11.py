class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == None:
            return 0
        count = 0
        for item in s[-1::-1]:
            if item == ' ':
                break
            count += 1
        return count
