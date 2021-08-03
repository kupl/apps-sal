class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        while n != 1:
            if n in nums:
                return False

            nums.add(n)
            s = str(n)
            new_n = 0
            for c in s:
                new_n += int(c) * int(c)
            n = new_n

        return True
