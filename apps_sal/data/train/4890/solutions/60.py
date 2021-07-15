def find_difference(a, b):
    c=1
    d=1
    for i in a:
        c*=i
    for i in b:
        d*=i
    return max(c-d, d-c)
