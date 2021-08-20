def hotpo(n):
    if n <= 0:
        return 0
    count = 0
    while n != 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
        count += 1
    return count
