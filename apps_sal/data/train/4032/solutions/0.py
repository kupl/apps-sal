from math import factorial as fac
def solve(n): return fac(2 * n) // fac(n) // fac(n + 1)
