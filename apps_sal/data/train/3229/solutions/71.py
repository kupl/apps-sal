def am_i_wilson(n): ### This is idiotic... 
    if n in [5, 13, 563]:
        return True
    else:
        return False
"""
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True  

def fac(n):
    count = 1
    for each in range(1, n + 1):
        print(count)
        count *= each
    return count

def am_i_wilson(n):
    print(n)
    if n in (0,1):
        return False
    if is_prime(n):
        tmp = (fac(n-1)+1)/(n**2)
        if tmp == int(tmp):
            return True
    else:
        return False 
"""
