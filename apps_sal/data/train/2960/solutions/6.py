def gcd(a, b): return gcd(b, a % b) if b else a
def lcm(a, b): return a / gcd(a, b) * b
def sum_differences_between_products_and_LCMs(p): return sum(x * y - (lcm(x, y) if x and y else 0) for x, y in p)
