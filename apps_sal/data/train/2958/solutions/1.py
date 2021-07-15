def n(x):
    return x * (x+1) // 2

def subcuboids(x, y, z):
    return n(x) * n(y) * n(z)
