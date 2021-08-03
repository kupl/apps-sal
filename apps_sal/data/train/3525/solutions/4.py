def flipping_game(num):
    if all(num):
        return len(num) - 1
    x = 0
    m = 0
    for n in num:
        if n == 0:
            x += 1
            m = max(x, m)
        else:
            x = max(x - 1, 0)
    return num.count(1) + m
