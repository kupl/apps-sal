def ip_to_int32(ip):
    return reduce(lambda p, n: (p << 8) + int(n), ip.split('.'), 0)
