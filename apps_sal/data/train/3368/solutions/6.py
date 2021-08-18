def circular_prime(n):

    l = len(str(n))

    for i in range(l):

        if is_prime(n):
            n = circul_num(n, l)
        else:
            return False
    return True


def circul_num(n, l):
    power = 10**(l - 1)

    if len(str(n)) < l:
        N = n * 10
    else:
        N = (n % power) * 10 + (n // power)
    return N


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
