def area_or_perimeter(l, w):
    if l == w:
        result = l ** 2
        return int(result)
    else:
        result = 2 * (l + w)
        return int(result)
