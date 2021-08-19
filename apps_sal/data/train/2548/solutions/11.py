class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
        '\n    #    my solution......a bit too slow....\n    \n         if num <= 0:\n             return False\n         if num in [1,2,3,4,5,6]:\n             return True\n         if self.isPrime(num):\n             return False\n         else:\n             i = 2\n             while i <= int(math.sqrt(num)):\n                 if num%i == 0:\n                     if (self.isPrime(i) and i not in [2,3,5]) or (self.isPrime(num//i) and num//i not in [2,3,5]):\n                         return False\n                 i += 1\n             return True\n             \n         \n         \n     def isPrime(self, n):\n         if n <= 1:\n             return False\n         for i in range(2, int(math.sqrt(n)) + 1):\n             if n % i == 0:\n                 return False\n         return True\n         '
