class Solution:

    def thirdMax(self, nums):
        a = b = c = -9999999999
        for n in nums:
            if n > c and n != b and (n != a):
                c = n
                if c > b:
                    (b, c) = (c, b)
                if b > a:
                    (a, b) = (b, a)
        if c == -9999999999:
            return a
        return c
