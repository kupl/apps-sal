class Solution:

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = b1 = a2 = b2 = 0
        a = a.split('+')
        b = b.split('+')
        a1 = int(a[0])
        a2 = int(b[0])
        b1 = int(a[1][:-1])
        b2 = int(b[1][:-1])
        a3 = a1 * a2 - b1 * b2
        b3 = a1 * b2 + b1 * a2
        return str(a3) + '+' + str(b3) + 'i'
