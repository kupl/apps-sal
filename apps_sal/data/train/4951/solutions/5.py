def ip_to_int32(ip):
    return sum(int(o) << (8 * i) for i, o in enumerate(ip.split(".")[::-1]))
