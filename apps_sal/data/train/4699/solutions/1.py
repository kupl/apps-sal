def spinning_rings(inner_max, outer_max):
    a,b,res = inner_max,1,1
    while a != b:
        a = (a + inner_max) % (inner_max+1)
        b = (b + 1) % (outer_max+1)
        res += 1
    return res
