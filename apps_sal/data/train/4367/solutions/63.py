def area_or_perimeter(l , w):
    '''determine if a shape is a square or a rectangle'''
    square = l * w
    if l == w:
        return square
    else:
        return l + l + w + w

