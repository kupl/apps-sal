def ipv4__parser(ip, m):
    (n, h) = ('', '')
    for (i, j) in zip(ip.split('.'), m.split('.')):
        r = int(''.join([str(int(k) & int(l)) for (k, l) in zip(bin(int(i))[2:].zfill(8), bin(int(j))[2:].zfill(8))]), 2)
        n += str(r) + '.'
        h += str(int(i) - r) + '.'
    return (n.strip('.'), h.strip('.'))
