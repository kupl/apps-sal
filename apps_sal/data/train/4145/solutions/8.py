def ipv4__parser(ip_addr, mask):
    net_addr = '.'.join([str(int(i) & int(m)) for i, m in zip(ip_addr.split('.'), mask.split('.'))])
    host_addr = '.'.join([str(int(i) - int(n)) for i, n in zip(ip_addr.split('.'), net_addr.split('.'))])
    return net_addr, host_addr
