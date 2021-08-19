class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        str_n = list(str(n))
        product = 1
        for char in str_n:
            product *= int(char)
        acc = 0
        for char in str_n:
            acc += int(char)
        return product - acc
