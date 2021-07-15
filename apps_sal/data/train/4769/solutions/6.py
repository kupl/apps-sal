def area(d, l):
    if d <= l: return 'Not a rectangle'
    a = l * (d ** 2 - l ** 2) ** 0.5
    return round(a, 2) if a % 1 else int(a)
