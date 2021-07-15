def area_or_perimeter(l,w):
    if l == w:
        area = l * w
        return (area)
    elif l!=w:
        perimeter = 2 * (l + w)
        return (perimeter)
    else:
        return 0
