from math import ceil


def is_prime(num):
    if num == 2:
        return True
    for i in range(2, ceil(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def factor_sum(num):
    while not is_prime(num):
        n = num
        factors_sum = 0
        while num % 2 == 0:
            factors_sum += 2
            num /= 2
        i = 3
        max_factor = num ** 0.5
        while i <= max_factor:
            while num % i == 0:
                factors_sum += i
                num /= i
                max_factor = num ** 0.5
            i += 2
        if num > 1:
            factors_sum += num
        if n == factors_sum:
            return n
        num = factors_sum
    return num
