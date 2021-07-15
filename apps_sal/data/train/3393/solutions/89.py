import math

def get_factors(m, n):
    cache = dict()
    for i in range(m, n + 1):
        factors = (j for j in range(1, 1 + i) if i % j == 0)
        total_sum = sum(j * j for j in factors)
        if math.sqrt(total_sum) % 1 == 0.:
            cache[i] = total_sum
    return cache
    
    
FACTORS = get_factors(1, 10000)

def list_squared(m, n):
    return [[i, FACTORS[i]] for i in range(m, n + 1) if i in FACTORS]

