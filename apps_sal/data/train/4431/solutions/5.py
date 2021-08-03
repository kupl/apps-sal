from string import ascii_lowercase as abc


def decode(message):
    cipher_map = dict(zip(list(abc[::-1]), list(abc)))

    return ''.join([cipher_map[c] if c in cipher_map else c for c in message])
