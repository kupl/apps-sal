def find_difference(a, b):
    aCube = a[0]*a[1]*a[2]
    bCube = b[0]*b[1]*b[2]
    return abs(aCube - bCube)
