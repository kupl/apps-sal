class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        c = 1
        clm = ''
        while n > 0:
            if (n % 26) > 0:
                clm = alph[(n % 26) - 1] + clm
                n = (n - (n % 26)) // 26
            elif (n % 26) == 0:
                clm = alph[25] + clm
                n = (n - 26) // 26
        return clm
