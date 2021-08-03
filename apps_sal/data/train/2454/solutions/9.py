class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        return self.convertToTitle((n - 1) // 26) + chr(ord('A') + (n - 1) % 26)
