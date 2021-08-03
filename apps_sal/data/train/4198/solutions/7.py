import re
from collections import Counter


def prime_factor(n):
    if n == 1:
        return Counter([1])
    factors = Counter()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n != 1:
        factors[n] = 1
    return factors


def simplify(n):
    a, b = 1, 1
    for k, v in prime_factor(n).items():
        while v >= 2:
            a *= k
            v -= 2
        b = b * k if v else b
    if a == 1:
        return f'sqrt {b}' if b > 1 else '1'
    if b == 1:
        return str(a)
    return f'{a} sqrt {b}'


def desimplify(s):
    res = re.match(r'(\d+ ?)?(sqrt (\d+))?', s)
    a, b = res.group(1), res.group(3)
    ans = int(a)**2 if a else 1
    return ans * int(b) if b else ans
