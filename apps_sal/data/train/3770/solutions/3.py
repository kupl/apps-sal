def to_1D(x, y, size):
    return y*size[0] + x
    
def to_2D(n, size):
    return divmod(n, size[0])[::-1]
