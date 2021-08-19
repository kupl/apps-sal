def area(d, l):
    if d <= l:
        return 'Not a rectangle'
    else:
        return round(l * (d ** 2 - l ** 2) ** (1 / 2), 2)
