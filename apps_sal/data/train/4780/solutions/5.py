from math import ceil, sqrt


def square_pi(digits):
    pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    return ceil(sqrt(sum((int(i) ** 2 for i in pi[:digits]))))
