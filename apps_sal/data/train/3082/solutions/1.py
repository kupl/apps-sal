def is_prime(n):
    """Return True if n is a prime number otherwise return False"""
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, n):
        if n % i == 0 and n != i:
            return False
    return True
