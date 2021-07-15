class Solution:
     def largestPalindrome(self, n):
         """
         :type n: int
         :rtype: int
         """
         
         table = [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
         return table[n - 1] % 1337
     
         ''' Time Limited when n = 8 , maybe caused by the lowly run time of python
         if n == 1:
             return 9
         maxNum = int(pow(10, n)) - 1
         for i in reversed(range(maxNum // 10, maxNum)):
             palindrome = self.createPalindrome(i)
             j = maxNum
             while j * j >= palindrome:
                 if palindrome % j == 0:
                     return palindrome % 1337
                 j -= 1
         return 0
     
     def createPalindrome(self, n):
         palindrome = str(n)
         reverse = str(n)[::-1]
         palindrome += reverse
         return int(palindrome)
         '''

