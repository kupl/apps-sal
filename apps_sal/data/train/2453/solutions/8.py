class Solution:
     def isHappy(self, n):
         """
         :type n: int
         :rtype: bool
         """
         slow, fast = n, n
         while True:
         	slow = self.getSquareSum(slow)
         	fast = self.getSquareSum(fast)
         	fast = self.getSquareSum(fast)
         	if slow == fast:
         		break;
         if slow == 1:
         	return True
         return False
 
     def getSquareSum(self, n):
     	return sum([int(i)**2 for i in str(n)]);
