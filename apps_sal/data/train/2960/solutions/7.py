from math import gcd

def sum_differences_between_products_and_LCMs(pairs):
    p=[x*y for x,y in pairs]
    lcd=[x*y/gcd(x,y) if y!=0 else 0 for x,y in pairs]
    return sum(x-y for y,x in zip(lcd,p))
