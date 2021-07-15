def spinning_rings(inner_max, outer_max):
    a,b,c = 0,0,0
    while True:
        a = (a - 1) % (inner_max + 1)
        b = (b + 1) % (outer_max + 1)
        c += 1
        if a == b: return c
