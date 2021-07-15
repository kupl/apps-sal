def is_prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def step(g, m, n):
    for i in range(m, n - g):
        if is_prime(i) and is_prime(i + g):
            return [i,i+g]
    return None
