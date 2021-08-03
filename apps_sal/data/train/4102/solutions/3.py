def prime_detector(x):
    if x >= 2:
        for y in range(2, int(x / 2)):
            if (x % y) == 0:
                return False
        return True
    else:
        return False


def odd_not_prime(n):
    i = 1
    odd_n_prime = 0
    while i <= n:
        if not prime_detector(i):
            odd_n_prime = odd_n_prime + 1
        i = i + 2
    return odd_n_prime
