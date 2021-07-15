def poly_add(a, b):
    lmax = max(len(a), len(b))
    a += [0]*(lmax - len(a))
    b += [0]*(lmax - len(b))    
    return list(map(sum, zip(a,b)))
