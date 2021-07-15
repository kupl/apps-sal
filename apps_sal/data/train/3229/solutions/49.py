from math import factorial as f

def is_prime(n):
    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True
    
def am_i_wilson(n):
    if n <= 1:
        return False
    if not is_prime(n):
        return False
    return (f(n-1) + 1) % (n*n) == 0
