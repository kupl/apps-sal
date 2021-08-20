import math


class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(num) for num in str(n)]
        return math.prod(digits) - sum(digits)
