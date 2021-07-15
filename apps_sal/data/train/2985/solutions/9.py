from math import gcd
def reflections(max_x, max_y):
    i=gcd(max_x,max_y)
    return (max_x//i+max_y//i)%2==0

