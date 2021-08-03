def area_or_perimeter(l, w):
    area_rectangle = l * w
    area_square = l * l
    perimeter_rectangle = 2 * (l + w)
    perimeter_square = 4 * l
    if l == w:
        return area_square
    else:
        return perimeter_rectangle
