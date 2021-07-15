import fractions
def binary_gcd(x, y):
    output = bin(fractions.gcd(x,y))
    return output.count('1')
