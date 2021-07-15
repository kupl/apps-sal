def limit(n):
    return max(0, min(2.375, n))


def passer_rating(a, y, c, t, i):
    Y = limit((y / a - 3) * 0.25)
    C = limit((c / a - 0.3) * 5)
    T = limit(20 * t / a)
    I = limit(2.375 - 25 * i / a)
    return round(100 * (Y + C + T + I) / 6, 1)
