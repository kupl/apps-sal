import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def div_num(a, b):
    div_num = []
    if a > b:
        return 'Error'
    for i in range(a, b + 1):
        div_num.append(len(list(divisorGenerator(i))))
    max_num = max(div_num)
    max_index = div_num.index(max_num)
    return a + max_index
