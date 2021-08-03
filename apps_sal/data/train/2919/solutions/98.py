from string import ascii_lowercase as letters


def encode(message, key):
    return [letters.index(m) + int(k) + 1 for m, k in zip(message, f'{key}' * len(message))]
