def ip_to_int32(ip):
    result = 0
    for s in ip.split('.'):
        result *= 256
        result += int(s)
    return result
