def area_or_perimeter(l, w):
    perimeter = 2 * l + 2 * w
    area = l * w
    if l == w:
        return area
    else:
        return perimeter
