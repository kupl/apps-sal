class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        L = "1"
        if(n == 1):
            return L
        while(n > 1):
            M = ""
            i = 0
            while(i < len(L)):
                k = 1
                x = L[i]
                while(i < len(L) - 1 and L[i + 1] == x):
                    i = i + 1
                    k = k + 1
                M = M + str(k) + x
                i = i + 1
            n = n - 1
            L = M
        return L
