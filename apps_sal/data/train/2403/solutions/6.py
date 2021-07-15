class Solution:
     def checkPerfectNumber(self, num):
         """
         :type num: int
         :rtype: bool
         """
         if num < 2:
             return False
         sum_ = 1
         for i in range(2, math.ceil(math.sqrt(num))):
             if num % i == 0:
                 sum_ += i + num // i
         return sum_ == num
