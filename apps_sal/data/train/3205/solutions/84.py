def is_divisible(n,x,y):
    a = n/x
    b = n/y
    cka = a - int(a)
    ckb = b - int(b)
    if cka > 0 or ckb > 0:
        return False
    else:
        return True
