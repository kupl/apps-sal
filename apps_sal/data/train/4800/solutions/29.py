def hotpo(n):
    counter = 0
    while n > 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
        counter += 1
    return counter
