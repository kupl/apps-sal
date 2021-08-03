def encode(message, key):
    return [ord(char) - 96 + int(str(key)[i % len(str(key))]) for i, char in enumerate(message)]
