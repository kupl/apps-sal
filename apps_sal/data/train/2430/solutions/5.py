class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n = bin(n)[2:]
        # a = n[0::2]
        # b = n[1::2]
        # return (a.count(a[0]) == len(a) if a else True) and (b.count(b[0]) == len(b) if b else True) and (a[0] != b[0] if a and b else True)
        return '00' not in bin(n) and '11' not in bin(n)
