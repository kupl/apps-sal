from math import sqrt


def list_squared(m, n):
    ret_list = []
    for i in range(m, n):
        sum_divisors_2 = sum(
            x ** 2 + (i / x) ** 2
            if x != i / x
            else x ** 2
            for x in range(1, int(sqrt(i)) + 1)
            if not i % x
        )
        if sqrt(sum_divisors_2).is_integer():
            ret_list.append([i, sum_divisors_2])
    return ret_list
