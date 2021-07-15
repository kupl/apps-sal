def ipv4_address(address):
    addr = address.split('.')
    if len(addr) != 4:
        return False
    for e in addr:
        try:
            a = int(e)
            if a > 255 or a < 0:
                return False
            if str(a) != e:
                return False
        except:
            return False
    return True
