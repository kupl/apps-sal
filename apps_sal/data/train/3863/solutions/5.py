from functools import reduce
def gcd(a, b): return gcd(b, a % b) if b else a


def final_attack_value(x, m): return reduce(lambda a, b: a + b if a >= b else a + gcd(a, b), m, x)
