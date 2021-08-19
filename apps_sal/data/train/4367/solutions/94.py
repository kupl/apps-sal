def area_or_perimeter(l, w):
    if l == w:
        area = l * w
        return area
    else:
        perimeter = l + l + w + w
        return perimeter
    return area_or_perimeter
