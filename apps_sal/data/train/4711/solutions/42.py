import math


def zeros(n):
    # The trailing zero's
    sum = 0
    # Corner case where there is no zero for sure and to eliminate negative or zero(log limitations)
    if n < 5:
        return 0
    # The algorithm from Wolfram
    for i in range(1, math.floor(math.log(n, 5) + 1)):
        sum += math.floor(n / pow(5, i))
    return sum
