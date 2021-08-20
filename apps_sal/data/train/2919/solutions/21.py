def encode(message, key):
    return [ord(s) - 96 + int(str(key)[i % len(str(key))]) for (i, s) in enumerate(message)]
