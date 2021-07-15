def area_or_perimeter(l: int, w: int) -> int:
    """ Get the area of a square or the perimeter of a rectangle. """
    return l * w if l == w else l * 2 + w * 2
