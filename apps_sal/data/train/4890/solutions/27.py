def find_difference(a, b):
    resa = a[0]
    resb = b[0]
    for i in a[1:]:
        resa = resa * i
    for i in b[1:]:
        resb = resb * i
    return abs(resa - resb)
