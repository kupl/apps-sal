def is_mac_48_address(address):
    L = address.split('-')
    if len(L) != 6:
        return False
    for x in L:
        try:
            int(x, 16)
        except:
            return False
    return True
