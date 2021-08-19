def area(d, l):
    c = (d * d - l * l) ** 0.5
    area = c * l
    if d <= l:
        return 'Not a rectangle'
    else:
        return round(area, 2)


area(6, 4)
