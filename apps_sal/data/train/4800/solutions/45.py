def hotpo(n):
    count = 0
    while True:
        if n < 2:
            return count
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
