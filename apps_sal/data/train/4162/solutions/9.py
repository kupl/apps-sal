def friends(n):
    x = 1
    while True:
        if n / 2 ** x <= 1:
            break
        x += 1
    return x - 1
