class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        total = 0

        while n > 0:
            num = n % 10
            prod *= num
            total += num
            n = n // 10
        return prod - total
