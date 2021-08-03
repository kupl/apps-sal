import math
from collections import Counter


def primeFactors(n):
    total = []
    while n % 2 == 0:
        total.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            total.append(i)
            n //= i

    if n > 2:
        total.append(n)
    return ''.join([f'({key}**{value})' if value > 1 else f'({key})' for key, value in Counter(total).items()])
