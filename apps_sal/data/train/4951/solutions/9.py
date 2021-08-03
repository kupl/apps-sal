def ip_to_int32(ip):
    return int(''.join([(format(int(i), "08b")) for i in ip.split('.')]), 2)
