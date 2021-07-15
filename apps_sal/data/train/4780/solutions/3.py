import math

pi_digits = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

def square_pi(digits):
    s = sum(d*d for d in map(int, pi_digits[:digits]))
    return math.ceil(s ** 0.5)
