def divisors(n):
    result = 1
    for i in range(n // 2):
        if n % (i + 1) == 0:
            result += 1
    return result
