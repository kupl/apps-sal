from math import factorial
def f(n):
    if type(n) != int: 
        return None
    else:
        if n<=0: 
            return None
        p=0
        for k in range(1,n+1):
            p+=k
        return p


