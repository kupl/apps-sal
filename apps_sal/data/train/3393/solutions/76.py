import math

def list_squared(m, n):
    result = []
    for x in range(m, n):
        divisors = make_divisors(x)
        squared_list = list(map(square, divisors))
        total = sum(squared_list)
        if math.sqrt(total).is_integer():
            result.append([x, total])
    return result
        
        
def square(n):
    return n * n
        
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
