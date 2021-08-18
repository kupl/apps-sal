def find_difference(a, b):
    v1 = a[0] * a[1] * a[2]
    v2 = b[0] * b[1] * b[2]
    if(v1 > v2):
        return v1 - v2
    else:
        return v2 - v1
