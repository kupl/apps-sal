def ipv4__parser(ip_addr, mask):
    host = []
    network = []

    ip_addr = [int(s) for s in ip_addr.split('.')]
    mask = [int(s) for s in mask.split('.')]

    for octet in range(4):
        host += [ip_addr[octet] & mask[octet]]
        network += [ip_addr[octet] & ~mask[octet]]

    host = [str(i) for i in host]
    network = [str(i) for i in network]

    return '.'.join(host), '.'.join(network)
