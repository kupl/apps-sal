import math


def sol_equa(n):
    # your code
    # x - 2y ...f1
    # x + 2y ...f2
    # A = sum(f1, f2) = 2x divisible by 2
    # B = diff(f1, f2) = 4y divisible by 4
    result = []
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            A = i + n / i
            B = abs(i - n / i)
            if A % 2 == 0 and B % 4 == 0:
                result.append([A / 2, B / 4])
    return result
