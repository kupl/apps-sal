def encode(message, key):
    key = list(map(int, str(key)))
    return [ord(c) - 96 + key[i % len(key)] for (i, c) in enumerate(message)]
