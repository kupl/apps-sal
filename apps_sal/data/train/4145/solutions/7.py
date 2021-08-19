def ipv4__parser(ip_addr, mask):
    (ip, sMask) = (ip_addr.split('.'), mask.split('.'))
    nb = [str(int(a) & int(b)) for (a, b) in zip(ip, sMask)]
    hi = [str(int(a) - int(b)) for (a, b) in zip(ip, nb)]
    return ('.'.join(nb), '.'.join(hi))
