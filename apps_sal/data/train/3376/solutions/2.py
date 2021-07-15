def square_free_part(n):
    if type(n) != int or n < 1:
        return
    while n % 4 == 0:
        n //= 2
    k = 3
    while k * k <= n:
        while n % (k*k) == 0:
            n //= k
        k += 2
    return n

