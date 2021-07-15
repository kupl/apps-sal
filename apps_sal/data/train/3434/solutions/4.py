def bin_mul(a, b):
    (b, a), r = sorted((a, b)), []
    while a:
        if a % 2 and b:
            r.append(b)
        a //= 2
        b *= 2
    return r[::-1]
