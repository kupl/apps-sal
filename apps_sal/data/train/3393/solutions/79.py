def divisors(n):
    divs = []
    for x in range(1, int(n**0.5)+1): 
        if n % x == 0:
            divs.extend([x**2, (n//x)**2])
    return sum(set(divs)) 
    
def list_squared(start, stop):
    squares = []
    for x in range(start, stop+1):
        x_sum = divisors(x)
        if int(x_sum**0.5) **2 == x_sum: 
            squares.append([x, x_sum])

    return squares

