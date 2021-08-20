def beeramid(bonus, price):
    if bonus < 0:
        return 0
    sum = 0
    x = 1
    c = 0
    while bonus / price >= sum:
        sum = sum + x ** 2
        x += 1
        c += 1
    return c - 1
