def subcuboids(x, y, z):
    l = x * (x + 1) // 2
    m = y * (y + 1) // 2
    n = z * (z + 1) // 2
    return int(l * m * n)
