def movie(a, b, c):
    import math
    for n in range(500000):
        if n * b > math.ceil(a + b * (1 - c ** n) / (1 - c)):
            return n - 1
