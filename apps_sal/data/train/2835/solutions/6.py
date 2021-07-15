def is_prime(n):
    for i in range(2, int(n**(1/2) +1)):
        if n % i == 0:
            return False
    return True

def solve(a, b):
    primeseries ="2"
    for i in range(3,41000,2):
        if is_prime(i):
          primeseries += (str(i))
    return primeseries[a:a+b]
