class Solution:
     def isHappy(self, n):
         """
         :type n: int
         :rtype: bool
         """
         def isHappyHelper(n):
             squaresum = 0
             while n:
                 n, remainder = divmod(n, 10)
                 squaresum += remainder**2
             if squaresum == 1:
                 return True
             elif squaresum in seenumbers:
                 return False
             else:
                 seenumbers.add(squaresum)
                 return isHappyHelper(squaresum)
             
         if n <= 0:
             return False
         seenumbers = set()
         seenumbers.add(n)
         return isHappyHelper(n)

