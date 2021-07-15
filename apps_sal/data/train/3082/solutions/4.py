def is_prime(n,i=2):
    if (n <= 2):
        return True if(n == 2) else False
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    return is_prime(n, i + 1)
