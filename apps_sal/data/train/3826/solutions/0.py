import math

def cycle(n) :
    if n % 2 == 0 or n % 5 ==0:
        return -1
    k = 1
    while pow(10,k,n) != 1:
        k += 1
    return k
            
    
       

