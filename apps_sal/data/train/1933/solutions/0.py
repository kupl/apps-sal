class Solution:

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        a[1] = a[1][:-1]
        b[1] = b[1][:-1]
        a = list(map(int, a))
        b = list(map(int, b))
        print((a, b))
        r = a[0] * b[0] - a[1] * b[1]
        i = a[1] * b[0] + a[0] * b[1]
        print((r, i))
        return '{0}+{1}i'.format(r, i)
