def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            return False
    return True

def gap(g, m, n):
    prev = n
    for i in range(m, n+1):
        if is_prime(i):
            if i - prev == g:
                return [prev, i]
            prev = i
    return None

