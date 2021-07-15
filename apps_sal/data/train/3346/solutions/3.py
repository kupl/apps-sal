def is_prime(a):
    return all(a % i for i in range(2, int(a**0.5)+1))
        
def gap(g, m, n):
    for a in range(m, n-g+1):
        if is_prime(a) and is_prime(a+g) and not any(is_prime(j) for j in range(a+1, a+g)):
            return [a, a+g]

