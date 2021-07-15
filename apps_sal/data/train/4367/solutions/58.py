def area_or_perimeter(l , w):
    square = (l*w)
    rectangle = 2*(l+w)
    if l == w:
        return square
    else:
        return rectangle
