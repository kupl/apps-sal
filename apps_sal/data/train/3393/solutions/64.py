import math


def list_squared(m, n):
    final = []
    for i in range(m, n):
        divisors = find_divisors(i)
        sum_sqrd = sum([d * d for d in divisors])
        if math.sqrt(sum_sqrd).is_integer():
            final.append([i, sum_sqrd])

    return final


def find_divisors(x):
    i = 1
    divisors = []
    while i <= math.sqrt(x):
        if x % i == 0:
            if x / i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(x / i))

        i += 1
    divisors.sort()
    return divisors
