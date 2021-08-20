class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        stringInt = str(n)
        product = 1
        sum = 0
        for i in stringInt:
            product *= int(i)
            sum += int(i)
        return product - sum
