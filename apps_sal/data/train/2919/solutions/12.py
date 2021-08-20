def encode(message, key):
    return [ord(sym) - 96 + int(str(key)[i % len(str(key))]) for (i, sym) in enumerate(message)]
