def zeros(n):
    import math
    if n == 0:
        return 0
    kmax = int(math.log(n, 5))
    return sum((int(n / math.pow(5, i)) for i in range(1, kmax + 1)))
