def ip_to_int32(ip):
    r = ""
    for i in ip.split('.'):
        r += "{0:08b}".format(int(i))
    return int(r, 2)
