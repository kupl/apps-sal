from numpy import prod
def is_smooth(n):
    number = n
    divisors = []
    while 1:
        if not n%2:
            divisors.append(2)
            n/=2
        else: break
        
    while 1:
        if not n%3:
            divisors.append(3)
            n/=3
        else: break

    while 1:
        if not n%5:
            divisors.append(5)
            n/=5
        else: break
        
    while 1:
        if not n%7:
            divisors.append(7)
            n/=7
        else: break
    
    if prod(divisors)==number and max(divisors) == 2: return "power of 2"
    elif prod(divisors)==number and max(divisors) == 3: return "3-smooth"
    elif prod(divisors)==number and max(divisors) == 5: return "Hamming number"
    elif prod(divisors)==number and max(divisors) == 7: return "humble number"
    else: return "non-smooth"
