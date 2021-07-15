def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    
def reduce_fraction(fraction):
    num, denom = fraction
    gcd_num_denom = gcd(num, denom)
    return (num // gcd_num_denom, denom // gcd_num_denom)
