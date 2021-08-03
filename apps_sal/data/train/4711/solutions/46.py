import math


def zeros(n):
    count = 0
    if n == 0:
        return 0
    else:
        k_max = math.floor(math.log(n, 5))
        for i in range(k_max):
            ans = math.floor(n / (5**(i + 1)))
            count = count + ans
        return count
