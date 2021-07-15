def beeramid(bonus, price):
    i = 0
    while bonus > 0:
        i += 1
        bonus -= price * i**2
        if bonus < 0: i -= 1
    return i
