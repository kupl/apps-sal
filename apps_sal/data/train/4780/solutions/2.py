from math import ceil
pi_digits = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'


def square_pi(digits):
    return ceil(sum((int(d) ** 2 for d in pi_digits[:digits])) ** 0.5)
