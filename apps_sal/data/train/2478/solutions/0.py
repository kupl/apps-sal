class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sums = sum([ord(i) for i in s]), sum([ord(i) for i in t])
        return chr(sum([ord(i) for i in t]) - sum([ord(i) for i in s]))
