def binary_gcd(x, y): 
    from fractions import gcd
    return bin(reduce(gcd, [x, y])).count("1")
