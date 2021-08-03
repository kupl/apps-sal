from fractions import gcd


def convergents_of_e(n):
    def b(n):
        return n // 3 * 2 if n % 3 == 0 else 1
    x, y = b(n), 1
    for k in range(n - 1, 0, -1):
        x, y = b(k) * x + y, x
    x = (x + y) // gcd(x + y, x)
    return sum(int(d) for d in str(x))
