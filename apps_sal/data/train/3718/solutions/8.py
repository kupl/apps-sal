def divisors(n):
    return len([x for x in range(1,(n//2)+1) if n % x == 0])+1
