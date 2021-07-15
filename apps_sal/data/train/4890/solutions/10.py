def find_difference(a, b):
    aVol = a[0] * a[1] * a[2]
    bVol = b[0] * b[1] * b[2]
    
    return abs(aVol - bVol)

