class Solution:

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = int(a.split('+')[0])
        b1 = int(a.split('+')[1][:-1])
        a2 = int(b.split('+')[0])
        b2 = int(b.split('+')[1][:-1])
        a = a1 * a2 - b1 * b2
        b = b1 * a2 + a1 * b2
        return str(a) + '+' + str(b) + 'i'
