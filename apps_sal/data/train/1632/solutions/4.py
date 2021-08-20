import math


def countOnes(left, right):

    def onesRangeDigit(n, digit):
        ex = 2 ** digit
        ones = ex * math.floor((n + 1) / (2 * ex)) + max((n + 1) % (2 * ex) - ex, 0)
        return ones

    def onesRange(n):
        ex = math.ceil(math.log(n + 1, 2))
        print(ex)
        ones = 0
        for i in range(ex):
            ones += onesRangeDigit(n, i)
        return ones
    return onesRange(right) - onesRange(left - 1)
