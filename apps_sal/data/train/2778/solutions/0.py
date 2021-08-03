def faro_cycles(n):
    x, cnt = 2, 1
    while x != 1 and n > 3:
        cnt += 1
        x = x * 2 % (n - 1)
    return cnt
