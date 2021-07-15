class Solution:
     def hammingDistance(self, x, y):
         """
         :type x: int
         :type y: int
         :rtype: int
         """
         
         hamming_distance=0
         
         while(x != 0 or y != 0):
             b1 = x & 1
             b2 = y & 1
             if(b1 != b2):
                 hamming_distance = hamming_distance+1
             x = x >> 1
             y = y >> 1
         
         return hamming_distance
