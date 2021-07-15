def poly_multiply(a, b):
    if a== [] or b== []:
        return []
    r=[0 for i in range(len(a)+len(b)-1)]
    for k,j in enumerate(a):
        for m,n in enumerate(b):
            r[k+m] += j*n    
    return r
