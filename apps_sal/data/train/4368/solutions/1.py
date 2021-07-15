from math import ceil

def cost(n):
    n -= 5
    
    if n<60 : return 30
    
    n -= 60
    
    return 30 + ceil(n/30) * 10
