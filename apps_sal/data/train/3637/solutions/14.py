def is_prime(a):
    if a < 4:
        return True
    for i in range(2,int(a/2)+1):
        if a%i == 0:
            return False
    return True

def num_primorial(n):
    result = 1
    count_primes = 0
    i = 2
    while count_primes < n:
        if is_prime(i):
            result *= i
            count_primes += 1
        i += 1
    return result
