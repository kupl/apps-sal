def area_or_perimeter(l, w):
    if l == w:
        polygon = 'square'
        return l ** 2
    else:
        polygon = 'rectangle'
        return l * 2 + w * 2
