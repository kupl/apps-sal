def int32_to_ip(int32):
    # your code here

    octets = []
    octets.append(str((int32 & 0xFF000000) >> 24))
    octets.append(str((int32 & 0x00FF0000) >> 16))
    octets.append(str((int32 & 0x0000FF00) >> 8))
    octets.append(str(int32 & 0x000000FF))
    return '.'.join(octets)
