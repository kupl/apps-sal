def find_difference(a, b):
    Va = a[1]*a[2]*a[0]
    Vb = b[1]*b[2]*b[0]
    diff = Va - Vb
    return diff if diff > 0 else -diff  
