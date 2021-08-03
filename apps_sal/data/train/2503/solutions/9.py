class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) < len(b):
            a, b = b, a
        l = len(a)
        c = -1
        for rg in range(1, l + 1):
            for i in range(l - rg + 1):
                s = a[i:i + rg]
                if b.find(s) == -1:
                    if len(s) > c:
                        c = len(s)
        return c
