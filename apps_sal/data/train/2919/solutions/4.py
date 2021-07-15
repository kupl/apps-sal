from itertools import cycle


def encode(message, key):
    return [ord(ch) - 96 + int(code) for
            ch, code in zip(message, cycle(str(key)))]
