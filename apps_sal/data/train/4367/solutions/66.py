def area_or_perimeter(l, w):
    rectangle_perimeter = 2 * (l + w)
    square_area = l * l
    if l == w:
        return square_area
    else:
        return rectangle_perimeter
