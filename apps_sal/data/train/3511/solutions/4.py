def find_key(encryption_key):
    n = int(encryption_key, 16)
    i = next(i for i in range(2, int(n**0.5)+1) if n % i == 0)
    return ((n//i) - 1) * (i - 1)
