class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n == 1:
            return True
        my_set = set()
        while n not in my_set:
            my_set.add(n)
            sq_sum = 0
            while n > 0:
                remain = n % 10
                print(('r', remain))
                sq_sum += int(remain * remain)
                n = int(n / 10)
            print(sq_sum)
            if sq_sum == 1:
                return True
            else:
                n = sq_sum
        return False
