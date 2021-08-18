def encode(message, key):
    return [ord(c) - 96 + int(str(key)[i % len(str(key))]) for i, c in enumerate(message)]
