def find_difference(a, b):
    aa = a[0]
    ab = a[1]
    ac = a[2]
    ba = b[0]
    bb = b[1]
    bc = b[2]
    return abs(aa * ab * ac - ba * bb * bc)
