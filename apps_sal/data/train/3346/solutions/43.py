import math


def prime(num):
    num_root = int(math.sqrt(num))
    for i in range(3, num_root + 1, 2):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def create_prime_list(m, n):
    if m % 2 == 0:
        start = m + 1
    else:
        start = m
    for num in range(start, n + 1, 2):
        if prime(num):
            yield num


def gap(g, m, n):

    prime_nums = create_prime_list(m, n)
    l = []
    l.append(next(prime_nums))
    l.append(next(prime_nums))
    if l[1] - l[0] == g:
        return [l[0], l[1]]
    i = 0
    try:
        while prime_nums:

            if l[i + 1] - l[i] == g:
                return [l[i], l[i + 1]]
            l.append(next(prime_nums))
            i += 1
    except:
        return None
