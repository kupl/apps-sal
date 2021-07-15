import math
def solve(s,g):
    return (math.gcd(s,g),s-math.gcd(s,g)) if s%g == 0 else -1
