def encode(message: str, key):
    return [ord(x) - 96 + int(str(key)[i % len(str(key))]) for (i, x) in enumerate(message.lower())]
