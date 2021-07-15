gcd = lambda x,y: gcd(y,x % y) if x and x%y else y
lcm = lambda x,y: x*y / gcd(x,y) if x*y else 0
def sum_differences_between_products_and_LCMs(pairs):
    return sum(x[0]*x[1] - lcm(x[0],x[1]) for x in pairs)
