def find_difference(a, b):
    qa = a[0] * a[1] * a[2]
    qb = b[0] * b[1] * b[2]
    return qa - qb if qa > qb else qb - qa
