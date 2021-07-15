def nth_chandos_number(n):
    b='{:b}'.format(n)
    r=0
    for d in b:
        r=r*5+int(d)*5
    return r
