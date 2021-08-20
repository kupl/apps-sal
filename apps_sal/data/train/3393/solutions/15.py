from math import floor, sqrt


def list_squared(m, n):
    result = []
    for number in range(m, n):
        divisors = set()
        for divisor in range(1, floor(sqrt(number)) + 1):
            if number % divisor == 0:
                divisors.add(divisor)
                divisors.add(number // divisor)
        divisorsum = sum((x * x for x in divisors))
        if sqrt(divisorsum) % 1 == 0:
            result.append([number, divisorsum])
    return result
