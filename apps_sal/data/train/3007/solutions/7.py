from functools import reduce

def divisors(n):    
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def consecutive_sum(n):
    return len([x for x in divisors(n) if x %2 != 0])

