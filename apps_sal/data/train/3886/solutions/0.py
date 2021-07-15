def is_prime(n):
    return n >= 2 and all(n%i for i in range(2, 1+int(n**.5)))
    
def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))
