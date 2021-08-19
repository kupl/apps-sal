def int32_to_ip(int32):
    octets = []
    octets.append(str((int32 & 4278190080) >> 24))
    octets.append(str((int32 & 16711680) >> 16))
    octets.append(str((int32 & 65280) >> 8))
    octets.append(str(int32 & 255))
    return '.'.join(octets)
