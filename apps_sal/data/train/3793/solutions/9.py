def triangle_type(a, b, c):
    h = max(a, b, c)
    return 0 if a+b+c <= 2*h else 1 if 2*h**2 < a**2+b**2+c**2 else 2 if 2*h**2 == a**2+b**2+c**2 else 3
