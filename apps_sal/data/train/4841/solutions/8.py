from math import pi
from math import sin

def simpson(n):
    
    f = lambda x : (3/2) * (sin(x) ** 3)
    
    b = pi
    a = 0
    
    h = (b-a)/n
    coeff = 1/3*h
    sum_a = 4 * sum([f(a + (2*i - 1)*h) for i in range(1, n//2 + 1)])
    sum_b = 2 * sum([f(a + 2*i * h) for i in range(1, n//2)])
    
    return coeff * (f(a) + f(b) + sum_a + sum_b)
