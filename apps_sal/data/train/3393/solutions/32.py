from math import sqrt
from math import ceil


def list_squared(m, n):
    # your code
    final_list = []
    for x in range(m, n):
        divisors_sq = 0
        for y in range(1, ceil(sqrt(x))):
            if x % y == 0:
                divisors_sq += y**2
                if x != 1:
                    divisors_sq += (x // y)**2
        if x == 1:
            divisors_sq = 1
        if round(sqrt(divisors_sq)) == sqrt(divisors_sq):
            final_list.append([x, divisors_sq])
    return final_list


list_squared(1, 250)
