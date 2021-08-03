encode = decode = lambda message, key: message.translate(str.maketrans(*mapping(key)))


def mapping(key):
    even, odd = key[::2] + key[::2].upper(), key[1::2] + key[1::2].upper()
    return (even + odd, odd + even)
