def to_1D(x, y, size):
    return size[0] * y + x
    
def to_2D(n, size):
    return divmod(n, size[0])[::-1]

