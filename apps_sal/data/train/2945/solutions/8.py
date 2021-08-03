def fortune(f0, p, c0, n, i):
    inf = c0
    money = f0
    for j in range(n - 1):
        money = int(money + money * (p / 100) - inf)
        inf = int(inf + inf * (i / 100))

    return True if money >= 0 else False
