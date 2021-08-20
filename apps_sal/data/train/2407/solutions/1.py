class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        product = 1
        su = 0
        for i in digits:
            product *= int(i)
            su += int(i)
        return product - su
