import math

def f(z, eps):
    return max(-1, math.log(eps)/math.log(math.hypot(z.real, z.imag)))
