# Python >= 3.6.0 only
def solve(a): return list(dict.fromkeys(reversed(a)))[::-1]
