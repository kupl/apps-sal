def ip_to_int32(ip):
    return int(''.join([bin(int(x))[2:].zfill(8) for x in ip.split('.')]), 2)
