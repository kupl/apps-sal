def divisors(n):
    x = 0
    number = n
    while n >= 1:
        if number % n == 0:
            x += 1
        n -= 1
    return x
