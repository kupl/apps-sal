def is_mac_48_address(a):
    return a.count(' ') == 0 and a.count('-') == 5 and (a[0] not in ['Z', 'G'])
