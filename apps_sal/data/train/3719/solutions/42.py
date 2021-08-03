def starting_mark(height):
    """ y = mx+b, always has, always will."""
    slope = (10.67 - 9.45) / (1.83 - 1.52)  # (d-d0)/(h - h0)
    return round(slope * (-1.83 + height) + 10.67, 2)
