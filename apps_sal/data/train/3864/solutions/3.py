def int32_to_ip(i):
    return '.'.join([str(x) for x in [i >> 24 & 0xFF,
                                      i >> 16 & 0xFF,
                                      i >> 8 & 0xFF,
                                      i & 0xFF]])
