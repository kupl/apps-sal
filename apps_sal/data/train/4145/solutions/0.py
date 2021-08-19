def ipv4__parser(addr, mask):
    return tuple(('.'.join((str(n) for n in a)) for a in zip(*((a & m, a & ~m) for (a, m) in zip((int(n) for n in addr.split('.')), (int(n) for n in mask.split('.')))))))
