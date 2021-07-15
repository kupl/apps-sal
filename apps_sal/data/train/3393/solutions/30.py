from math import sqrt

def divisors_squared(x):
    l2 = []
    y = int(sqrt(x))
    for a in range(1, y+1):
        if x % a == 0:
            divby = x//a
            if a != divby:
                l2.extend((a**2, divby**2))
            else:
                l2.append(a)
    return l2

def list_squared(x, y):
    arr = []
    for i in range(x, y+1):
        z = sum(divisors_squared(i))
        if (sqrt(z)).is_integer():
            arr.append([i, z])
    return arr 

