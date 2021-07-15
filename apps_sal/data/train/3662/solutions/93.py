def xor(a,b):
    c = 0
    if a:
        c += 1
    if b:
        c += 1
    if c == 1:
        return True
    else:
        return False

