def encode(message, key):
    return [ord(c) - ord('`') + int(str(key)[i % len(str(key))]) for (i, c) in enumerate(message)]
