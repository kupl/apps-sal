class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        prod = 1
        for n in digits:
            prod *= n
        summ = 0
        for n in digits:
            summ += n
        return prod - summ
