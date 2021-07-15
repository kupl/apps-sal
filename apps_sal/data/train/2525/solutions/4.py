class Solution:
     def hammingDistance(self, x, y):
         """
         :type x: int
         :type y: int
         :rtype: int
         """
         x_b = '{:32b}'.format(x).replace(' ', '0')
         y_b = '{:32b}'.format(y).replace(' ', '0')
         
         count = 0
         for i in range(len(x_b)):
             if x_b[i] != y_b[i]:
                 count += 1
         return count

