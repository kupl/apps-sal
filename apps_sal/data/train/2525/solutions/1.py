class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0
        bin_x, bin_y = bin(x)[2:], bin(y)[2:]
        if x < y:
            bin_x = bin_x.zfill(len(bin_y))
        else:
            bin_y = bin_y.zfill(len(bin_x))
        return sum([abs(int(bin_x[i]) - int(bin_y[i])) for i in range(len(bin_x))])
