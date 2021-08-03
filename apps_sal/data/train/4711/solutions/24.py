def zeros(n):
    import math
    return 0 if n == 0 else sum((int(n * 5**-i)) for i in range(1, 1 + int(math.log(n, 5))))
