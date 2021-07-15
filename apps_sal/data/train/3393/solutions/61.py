import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def is_square(n):
    if n == 0:return True
    if n == 1:return True
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def list_squared(m, n):
    out = []
    for a in range(m, n+1):
        divisor_sum = sum(int(r*r) for r in list(divisorGenerator(a)))
        if is_square(divisor_sum):
            out.append([a, divisor_sum])
    return out

