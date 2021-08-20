def ip_to_int32(ip):
    retInt = 0
    octets = ip.split('.')
    for (ndx, offset) in enumerate((24, 16, 8, 0)):
        retInt = retInt | int(octets[ndx]) << offset
    return retInt
