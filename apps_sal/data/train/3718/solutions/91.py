def divisors(n):
    divs = 1
    print(round(n/2))
    for i in range(1, round(n/2)+1):
        if n % i == 0: divs+=1
    return divs
