def is_prime(num):
    'Return True if n is a prime number otherwise return False'
    return num > 1 and not any(num % n == 0 for n in range(2, num))
