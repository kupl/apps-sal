def is_mac_48_address(address):
    try:
        bytes = address.split("-")
        return all(0 <= int(byte, 16) < 256 for byte in bytes) and len(bytes) == 6
    except:
        return False
