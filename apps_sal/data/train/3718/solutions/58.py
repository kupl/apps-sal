import math
def divisorGenerator(n):       #求所有除数
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
def divisors(n):
    return len(list(divisorGenerator(n)))
