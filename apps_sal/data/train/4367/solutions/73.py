def area_or_perimeter(l, w):
    s = l * w
    p = (l + w) * 2
    if l == w:
        return s
    else:
        return p
