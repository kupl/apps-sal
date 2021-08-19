def hotpo(n):
    for i in range(999):
        if n == 1:
            return i
        if n % 2:
            n = n * 3 + 1
        else:
            n = n / 2
