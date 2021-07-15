def find_difference(a, b):
    la = len(a)
    reza = 1
    rezb = 1
    for i in range(la):
        reza *= a[i]
        rezb *= b[i]
    return abs(reza - rezb)
