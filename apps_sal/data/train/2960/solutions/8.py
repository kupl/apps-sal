from math import gcd

def sum_differences_between_products_and_LCMs(pairs):
    return sum((x[0]*x[1]-(x[0]*x[1]/(gcd(x[0],x[1])if x[1]!=0 else 1))) for x in pairs)
