import binascii


def hex_to_dec(s):
    return int.from_bytes(binascii.unhexlify(("0" * (len(s) % 2)) + s), byteorder="big")
