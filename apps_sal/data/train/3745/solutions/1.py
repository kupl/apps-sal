from string import ascii_lowercase


def encode_decode(message, key, shift, func):
    keys = ''.join(dict.fromkeys(key)) + ''.join((c for c in ascii_lowercase if c not in key))
    for c in message:
        if c.islower():
            (c, shift) = func(keys, c, shift)
        yield c


def encode(message, key, shift):
    return ''.join(encode_decode(message, key, shift, lambda k, c, s: (k[(k.find(c) + s) % 26], k.find(c) + 1)))


def decode(message, key, shift):
    return ''.join(encode_decode(message, key, shift, lambda k, c, s: (k[(k.find(c) - s) % 26], k.find(k[(k.find(c) - s) % 26]) + 1)))
