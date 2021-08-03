def hotpo(n):
    counter = 0
    if n != 1:
        counter += 1
        counter += hotpo(n / 2 if n % 2 == 0 else 3 * n + 1)
    return counter
