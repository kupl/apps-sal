from string import ascii_lowercase as alpha


def encode(message, key):
    key = (len(message) // len(str(key)) + 1) * str(key)
    return [alpha.index(c) + int(k) + 1 for (c, k) in zip(message, key)]
