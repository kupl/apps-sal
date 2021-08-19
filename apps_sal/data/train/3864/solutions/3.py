def int32_to_ip(i):
    return '.'.join([str(x) for x in [i >> 24 & 255, i >> 16 & 255, i >> 8 & 255, i & 255]])
