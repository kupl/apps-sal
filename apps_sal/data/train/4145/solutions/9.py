def to_int(n):
    return sum(int(i) * 256 ** e for (e, i) in enumerate(reversed(n.split('.'))))


def to_ip(n):
    return '.'.join(str((n // (256 ** e)) & 255) for e in range(3, -1, -1))


def ipv4__parser(ip_addr, mask):
    addr = to_int(ip_addr)
    mask = to_int(mask)
    return to_ip(addr & mask), to_ip(addr & ~mask)
