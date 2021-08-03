def is_prime(n):
    if n == 1:
        return False
    elif n == 3:
        return True
    else:
        for i in range(3, round(n**0.5) + 2):
            if n % i == 0:
                return False
        else:
            return True


def odd_not_prime(n):
    lst = list(range(1, n + 1, 2))
    return len([i for i in lst if not is_prime(i)])
