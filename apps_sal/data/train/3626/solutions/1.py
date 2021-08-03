def encode(message, key):
    a, b = (f"{key[i::2]}{key[i::2].upper()}" for i in (0, 1))
    return message.translate(str.maketrans(f"{a}{b}", f"{b}{a}"))


decode = encode
