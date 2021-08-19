def is_mac_48_address(address):
    return bool(__import__('re').match('-'.join(['[0-9A-F]{2}'] * 6) + '$', address))
