def reverse_bits(n):
    a = '{0:08b}'.format(n)
    b = list(a)
    b.reverse()
    c = ''
    for i in b:
        c += i
    return int(c, 2)
