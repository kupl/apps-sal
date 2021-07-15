def ip_to_int32(ip):
    return reduce(lambda acc, x: acc << 8 | x, (int(x) for x in ip.split('.')))
