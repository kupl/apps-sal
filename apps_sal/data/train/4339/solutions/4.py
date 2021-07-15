def roots(a ,b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        return round(-b / a, 2)
