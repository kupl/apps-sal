def is_prime(n):
    if n in (2, 3, 5):
        return True
    elif n < 5:
        return False
    elif n % 2:
        i = 3
        flag = True
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    else:
        return False


def nextPrime(n):
    i = n + 1
    while not is_prime(i):
        i += 1
    return i
