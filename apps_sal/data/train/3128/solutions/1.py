def is_mac_48_address(address):
    chunks = address.split('-')
    for chunk in chunks:
        try:
            int(chunk, 16)
        except ValueError:
            return False
    return len(chunks) == 6

