def area_or_perimeter(l, w):
    if l == w:
        return l * w
    elif l < w or l > w:
        return l * 2 + w * 2
