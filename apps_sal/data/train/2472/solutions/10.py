class Solution:

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and s.count('LLL') == 0
