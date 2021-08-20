def get_positions(n):
    (n, x) = divmod(n, 3)
    (n, y) = divmod(n, 3)
    (n, z) = divmod(n, 3)
    return (x, y, z)
