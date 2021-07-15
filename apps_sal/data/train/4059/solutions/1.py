def switch_lights(a):
    n = sum(a)
    for i, x in enumerate(a):
        if n % 2:
            a[i] ^= 1
        n -= x
    return a
