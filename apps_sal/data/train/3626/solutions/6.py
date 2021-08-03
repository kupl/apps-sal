def encode(message, key):
    x, y = key[::2] + key[::2].upper(), key[1::2] + key[1::2].upper()
    return message.translate(str.maketrans(x + y, y + x))


decode = encode
