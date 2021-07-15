def ipv4__parser(ip_addr, mask):
    arr = [(int(p), int(m)) for p, m in zip(ip_addr.split('.'), mask.split('.'))]
    return ('.'.join(str(a & b) for a, b in arr), '.'.join(str(a & b ^ a) for a, b in arr))
