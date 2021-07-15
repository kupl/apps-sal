def divisors(n):
    divs = 0
    
    for x in range(1, int(n**0.5)+1):
        if n % x == 0:
            divs += 2
    
    return divs - (x*x == n)
