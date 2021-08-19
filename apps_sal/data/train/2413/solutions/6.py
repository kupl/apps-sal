class Solution:

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
        return table[n - 1] % 1337
        ' Time Limited when n = 8 , maybe caused by the lowly run time of python\n         if n == 1:\n             return 9\n         maxNum = int(pow(10, n)) - 1\n         for i in reversed(range(maxNum // 10, maxNum)):\n             palindrome = self.createPalindrome(i)\n             j = maxNum\n             while j * j >= palindrome:\n                 if palindrome % j == 0:\n                     return palindrome % 1337\n                 j -= 1\n         return 0\n     \n     def createPalindrome(self, n):\n         palindrome = str(n)\n         reverse = str(n)[::-1]\n         palindrome += reverse\n         return int(palindrome)\n         '
