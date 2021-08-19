import math


def prime_test(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 'not_prime'
        else:
            continue
    return 'prime'


def gap(g, m, n):
    current_number = m
    while True:
        if current_number > n:
            return None
        if prime_test(current_number) == 'not_prime':
            current_number = current_number + 1
        elif prime_test(current_number + g) == 'not_prime':
            current_number = current_number + 1
        else:
            prime_in_between = 0
            for i in range(current_number + 2, current_number + g):
                if prime_test(i) == 'prime':
                    prime_in_between = i
                    break
                else:
                    continue
            if prime_in_between == 0:
                return [current_number, current_number + g]
            else:
                current_number = current_number + 1
