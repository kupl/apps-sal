class Solution:
     def hammingDistance(self, x, y):
         """
         :type x: int
         :type y: int
         :rtype: int
         """
         x_bits = [int(i) for i in bin(x)[2:]]
         y_bits = [int(j) for j in bin(y)[2:]]
         digit_diff = abs(len(x_bits)-len(y_bits))
 
         if len(y_bits) > len(x_bits):
             x_bits = [0] * digit_diff + x_bits
         elif len(x_bits) > len(y_bits):
             y_bits = [0] * digit_diff + y_bits
 
         hamming_dist = 0
         for i in range(0, len(x_bits)):
             if x_bits[i] != y_bits[i]:
                 hamming_dist += 1
 
         return hamming_dist

