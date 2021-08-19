def is_prime(n):
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    else:
        return True
