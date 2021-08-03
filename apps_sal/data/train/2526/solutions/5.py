class Solution:
    def trailingZeroes(self, n):
        two = 0
        five = 0
        tmp = n
        while tmp != 0:
            tmp = tmp // 5
            five = five + tmp
        tmp = n
        while tmp != 0:
            tmp = tmp // 2
            two = two + tmp
        res = min(five, two)
        return res
        """
         :type n: int
         :rtype: int
         """
