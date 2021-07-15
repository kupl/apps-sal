import math

def simpson(n):
    a, b = 0, math.pi
    f = lambda x: (3/2) * (math.sin(x) ** 3)
    h = (b - a) / n
    res = f(a)
    res += 4 * sum(f(a + i*h) for i in range(1, n, 2))
    res += 2 * sum(f(a + i*h) for i in range(2, n, 2))
    res += f(b)
    return (h / 3) * res
