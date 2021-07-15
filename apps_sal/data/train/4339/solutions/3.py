def roots(a,b,c):
    # your code
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return (-b + d**0.5)/(2*a) * 2
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        return round(x1 + x2, 2)


