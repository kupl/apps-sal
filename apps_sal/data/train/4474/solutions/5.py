def start_smoking(bars, boxes):
    a = []
    x = 180 * bars + 18 * boxes
    a.append(x + x // 5)
    n = x % 5 + x // 5
    while n >= 5:
        a.append(n // 5)
        n = n % 5 + n // 5
    return sum(a)
