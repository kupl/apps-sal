class Solution:

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        (a_r, a_u) = self.parse_str(a)
        (b_r, b_u) = self.parse_str(b)
        res_r = a_r * b_r - a_u * b_u
        res_u = a_r * b_u + a_u * b_r
        return '{0}+{1}i'.format(res_r, res_u)

    def parse_str(self, str):
        strs = str.split('+')
        real = int(strs[0])
        unreal = int(strs[1][:-1])
        return (real, unreal)
