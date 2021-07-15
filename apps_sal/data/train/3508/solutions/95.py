import math
def halving_sum(n): 
    # your code here
    number = n
    
    while number >= 1:
        n += (math.floor(number/2))
        number /= 2
        
    return n
