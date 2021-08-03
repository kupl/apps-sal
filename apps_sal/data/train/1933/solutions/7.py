class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a1 = int(a.split('+')[0])
        a2 = int(a.split('+')[1].replace('i', ''))
        b1 = int(b.split('+')[0])
        b2 = int(b.split('+')[1].replace('i', ''))

        m1 = a1 * b1 - a2 * b2
        m2 = a1 * b2 + a2 * b1

        return str(m1) + '+' + str(m2) + 'i'
