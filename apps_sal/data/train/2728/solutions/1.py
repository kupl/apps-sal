def gcd_ext(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = gcd_ext(b, a % b)
        return y, x - y * (a // b), gcd


def inverseMod(a, n):
    x, y, gcd = gcd_ext(a, n)
    if gcd == 1:
        return x % n
    else:
        return None
