from math import ceil

def layers(n):
    r = ceil(n**0.5)    
    return (r + (1 if r % 2 else 2)) // 2    
