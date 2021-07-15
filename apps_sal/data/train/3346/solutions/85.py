import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)): 
        if (num % i) == 0: 
            return False
    else: 
        return True



def gap(g, m, n):
    last_prime = 2
    for i in range(m,n):
        if is_prime(i):
            if i - last_prime == g:
                return [last_prime, i]
            last_prime = i
    return None
    


