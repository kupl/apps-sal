def shorter_reverse_longer(a,b):
    if len(a) >= len(b):
       return b + a[::-1] + b
    else:
        return a + b[::-1] + a
