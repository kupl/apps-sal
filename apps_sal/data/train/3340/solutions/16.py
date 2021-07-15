import math
def max2pow(n):
    even = 1
    while n % 2 == 0:
        even *= 2
        n /= 2
    return even, n

def sharkovsky(a, b):
    if a == b:
        return False
    even_a, odd_a = max2pow(a)
    even_b, odd_b = max2pow(b)
    if odd_a == 1 and odd_b == 1:
        return even_a > even_b
    if odd_a == 1 or odd_b == 1:
        return odd_b == 1    
    if even_a == even_b:
        return odd_a < odd_b
    return even_a < even_b
    

