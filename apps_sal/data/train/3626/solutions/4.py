def encode(message, key):
    tbl = str.maketrans(key[::2] + key[::2].upper() + key[1::2] + key[1::2].upper(), key[1::2] + key[1::2].upper() + key[::2] + key[::2].upper())
    return message.translate(tbl)


decode = encode
