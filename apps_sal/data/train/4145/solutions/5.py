def ipv4__parser(ip_addr, mask):
    host = []
    network = []

    # convert string addresses to a list of integers
    ip_addr = [int(s) for s in ip_addr.split('.')]
    mask = [int(s) for s in mask.split('.')]

    # calculate host and network addresses
    for octet in range(4):
        host += [ip_addr[octet] & mask[octet]]
        network += [ip_addr[octet] & ~mask[octet]]
    
    # convert list of integers to strings
    host = [str(i) for i in host]
    network = [str(i) for i in network]

    return '.'.join(host), '.'.join(network)
