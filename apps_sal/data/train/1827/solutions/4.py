#
 # [483] Smallest Good Base
 #
 # https://leetcode.com/problems/smallest-good-base/description/
 #
 # algorithms
 # Hard (33.74%)
 # Total Accepted:    6.7K
 # Total Submissions: 20K
 # Testcase Example:  '"13"'
 #
 # For an integer n, we call k>=2 a good base of n, if all digits of n base k
 # are 1.
 # Now given a string representing n, you should return the smallest good base
 # of n in string format.
 #
 # Example 1:
 #
 # Input: "13"
 # Output: "3"
 # Explanation: 13 base 3 is 111.
 #
 #
 #
 # Example 2:
 #
 # Input: "4681"
 # Output: "8"
 # Explanation: 4681 base 8 is 11111.
 #
 #
 #
 # Example 3:
 #
 # Input: "1000000000000000000"
 # Output: "999999999999999999"
 # Explanation: 1000000000000000000 base 999999999999999999 is 11.
 #
 #
 #
 # Note:
 #
 # The range of n is [3, 10^18].
 # The string representing n is always valid and will not have leading zeros.
 #
 #
 #
 from math import log
 class Solution:
     def smallestGoodBase(self, n):
         """
         :type n: str
         :rtype: str
         """
         num = int(n)
         bit = int(log(10, 2) * len(n) + 1)
         while bit > 0 :
             low, high = 2, int(num ** (1.0 / bit) + 1)
             while low <= high :
                 base = low + (high - low) // 2
                 tmp = 0
                 for _ in range(bit + 1) :
                     tmp = tmp * base + 1
                 # print(bit, low, high, base, tmp)
                 if tmp == num :
                     return str(base)
                 elif tmp < num :
                     low = base + 1
                 else :
                     high = base - 1
             bit -= 1
         return str(num - 1)

