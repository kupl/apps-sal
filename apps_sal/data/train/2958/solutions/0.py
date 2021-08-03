def subcuboids(x, y, z):
    return x * y * z * (x + 1) * (y + 1) * (z + 1) // 8
