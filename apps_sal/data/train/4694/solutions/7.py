from math import factorial    
def sum_fib(n):
    a = 1
    b = 1
    s = 2
    i = 2
    while i < n:  
        a, b = b, a+b    
        s += factorial(a)
        i+=1
    return s

