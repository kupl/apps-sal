def area_or_perimeter(l, w):
    if l == w:
        res = l * w
    else:
        res = l + l + w + w
    return res
