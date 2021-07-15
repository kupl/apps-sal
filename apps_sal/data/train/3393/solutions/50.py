import math

def divisors(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                yield n/i

def list_squared(m, n):
    ret = []
    for i in range(m, n+1):
        div_sum = sum([j**2 for j in divisors(i)])
        if math.sqrt(div_sum).is_integer():
            ret.append([i, div_sum])
    return ret

