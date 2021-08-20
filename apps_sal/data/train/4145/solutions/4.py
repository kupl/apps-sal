def ipv4__parser(ip_addr, mask):
    net_addr = '.'.join((str(int(a) & int(b)) for (a, b) in zip(ip_addr.split('.'), mask.split('.'))))
    host_addr = '.'.join((str(int(a) & 255 - int(b)) for (a, b) in zip(ip_addr.split('.'), mask.split('.'))))
    return (net_addr, host_addr)
