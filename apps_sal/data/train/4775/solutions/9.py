def fusc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return int(fusc(n / 2))
    if n % 2 != 0:
        return int(fusc((n - 1) / 2)) + int(fusc((n - 1) / 2 + 1))
