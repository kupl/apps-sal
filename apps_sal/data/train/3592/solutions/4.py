from math import gcd


def nearest(m="g"):
    def side(x, y, n):
        z = x * y // gcd(x, y)
        return (n + (z if m == "s" else -1)) // z * z
    return side


smallest = nearest("s")
greatest = nearest()
