def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def next_prime(n):
    i = n + 1
    while not is_prime(i):
        i += 1
    return i

