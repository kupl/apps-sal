def divisors(n):
    x = 1
    count = 2
    while True:
        if count > n: break
        if n % count == 0:
            x += 1
        count += 1
    return x
