import math


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        total = 0
        howMany = math.floor(m / n)
        print(howMany)
        if m % n == 0:
            for i in range(howMany - 1):
                total = total + n * (i + 1)
        else:
            for i in range(howMany):
                total = total + n * (i + 1)
        return total
    pass
