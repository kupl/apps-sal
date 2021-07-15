def divisors(n):
    
    num = []
    for x in range (1,n+1):
        if n % x == 0:
            num.append(x)
        else:
            continue
            
    return len(num)

