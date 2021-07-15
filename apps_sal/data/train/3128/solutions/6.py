def is_mac_48_address(address):
    try:
        return all(isinstance(int(x, 16),int) for x in address.split('-')) and len(address) == 17
    except:
        return False
