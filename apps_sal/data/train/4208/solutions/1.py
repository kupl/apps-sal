def ip_to_int(ip):
    return sum((int(i[0]) << i[1] * 8 for i in zip(ip.split('.'), range(3, -1, -1))))


def int_to_ip(num):
    return '.'.join((str(num >> i * 8 & 255) for i in range(3, -1, -1)))


def ipsubnet2list(subnet):
    (net, prelen) = subnet.split('/')
    (num, mask) = (ip_to_int(net), 1 << 32 - int(prelen))
    if net != int_to_ip(num):
        return None
    if mask == 2:
        return [int_to_ip(num), int_to_ip(num + 1)]
    return [int_to_ip(num ^ i) for i in range(1, mask - 1)]
