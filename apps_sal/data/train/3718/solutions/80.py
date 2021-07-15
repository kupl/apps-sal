def divisors(n):
    import math
    a = 0
    for i in range(n):
        if i >= 1:
            if n % i == 0:
                a += 1
    return a + 1
