from numpy import polymul

def poly_multiply(p1, p2):
    if not (p1 and p2 and any(p1) and any(p2)): return []
    return polymul(p1, p2).tolist()
