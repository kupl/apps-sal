import math


def sol_equa(n):
    result = []
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            A = i + n / i
            B = abs(i - n / i)
            if A % 2 == 0 and B % 4 == 0:
                result.append([A / 2, B / 4])
    return result
