def hotpo(n):
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
    return cnt
