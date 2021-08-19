import math


def primeFactors(n: int) -> str:
    list_result = []
    while n % 2 == 0:
        n = n / 2
        list_result.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            list_result.append(i)
    if n > 2:
        list_result.append(int(n))
    return ''.join([f'({i})' if list_result.count(i) == 1 else f'({i}**{list_result.count(i)})' for i in sorted(list(set(list_result)))])
