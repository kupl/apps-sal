class Solution:

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        a1 = int(a[0])
        a2 = int(a[-1][:-1])
        b1 = int(b[0])
        b2 = int(b[-1][:-1])
        print(a1)
        print(a2)
        c1 = a1 * b1 - a2 * b2
        c2 = a1 * b2 + a2 * b1
        return str(c1) + '+' + str(c2) + 'i'
