class Solution:

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = format(x, '#035b')
        y_bin = format(y, '#035b')
        print('x_bin: ', x_bin)
        print('y_bin: ', y_bin)
        hammingDistance = 0
        for (idx, val) in enumerate(x_bin):
            print('val: ', val)
            print('y_bin[idx]: ', y_bin[idx])
            if val != y_bin[idx]:
                hammingDistance += 1
        return hammingDistance
