def is_triangle(x, y, z):
    return (x < y + z) and (y < x + z) and (z < x + y)
