def gap(g, m, n):
    
    def prime(p):
        for i in range(2,int(p**0.5+1)):
            if p%i == 0:
                return False
        return True
    
    prev_prime = n
    for i in range(m,n+1):
        if prime(i):
            if i - prev_prime == g: 
                return [prev_prime, i]
            prev_prime = i

