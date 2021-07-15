def encode(str, key):
    """Translate str using given key"""
    switched = []
    for x in range(int(len(key) / 2)):
        switched.append(key[x * 2 + 1])
        switched.append(key[x * 2])
    switched = "".join(switched)
    return str.translate(str.maketrans(key + key.upper(), switched + switched.upper()))


def decode(str, key):
    """Do the same as encode"""
    return encode(str, key)
