class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        "\n         if s == None: return 0\n         count = 0\n         for item in s[-1::-1]:\n             if item == ' ':\n                 break\n             count += 1\n         return count\n         "
        count = len(s.strip().split(' ')[-1])
        return count
