class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

   #    public CONCISE solution....

        if num <= 0:
            return False
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1

        """
    #    my solution......a bit too slow....
    
         if num <= 0:
             return False
         if num in [1,2,3,4,5,6]:
             return True
         if self.isPrime(num):
             return False
         else:
             i = 2
             while i <= int(math.sqrt(num)):
                 if num%i == 0:
                     if (self.isPrime(i) and i not in [2,3,5]) or (self.isPrime(num//i) and num//i not in [2,3,5]):
                         return False
                 i += 1
             return True
             
         
         
     def isPrime(self, n):
         if n <= 1:
             return False
         for i in range(2, int(math.sqrt(n)) + 1):
             if n % i == 0:
                 return False
         return True
         """
