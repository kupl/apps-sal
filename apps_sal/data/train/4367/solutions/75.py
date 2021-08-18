def area_or_perimeter(l, w):
    l = int(l)
    w = int(w)

    if l == w:
        return l * w
    else:
        return l + l + w + w
