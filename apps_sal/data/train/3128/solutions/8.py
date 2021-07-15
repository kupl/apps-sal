def is_mac_48_address(address):
    try:
        return len([int(e, 16) for e in address.split('-')]) == 6
    except (ValueError, TypeError):
        return False
