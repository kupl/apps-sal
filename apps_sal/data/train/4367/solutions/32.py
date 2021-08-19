def area_or_perimeter(l, w):
    if l == w:  # check square or rectangle
        result = l**2
        return int(result)
    else:
        result = 2 * (l + w)
        return int(result)
