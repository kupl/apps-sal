def ipsubnet2list(subnet):
    netaddr, prefix = subnet.split('/')
    if not all([0 <= int(x) < 256 for x in netaddr.split('.')]):
        return None
    netaddrbyte = 0
    for x in netaddr.split('.'):
        netaddrbyte = netaddrbyte * 256 + int(x)
    r = []
    for i in range(2**(32 - int(prefix))):
        addr = netaddrbyte + i
        a = []
        for _ in range(4):
            a.append(addr % 256)
            addr //= 256
        r.append('.'.join(map(str, a[::-1])))
    if int(prefix) < 31:
        r = r[1:-1]
    return r
