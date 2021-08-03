class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, str(n)))
        sum_1 = 0
        product = 1
        result = 0
        for i in n:
            sum_1 += i
            product *= i
            result = product - sum_1
        return result
