def shift_left(a, b, n=0):
    if a == b:
        return n
    elif len(a)>len(b):
        return shift_left(a[1:], b, n + 1)
    else:
        return shift_left(a, b[1:], n + 1)
        

