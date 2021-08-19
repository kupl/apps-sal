def area(d, l):
    return 'Not a rectangle' if d <= l else round(l * (d * d - l * l) ** 0.5, 2)
