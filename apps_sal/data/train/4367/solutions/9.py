def area_or_perimeter(l, w):
    resu = 0
    if l == w:
        resu = l * w
        return resu
    else:
        resu = 2 * (l + w)
        return resu
