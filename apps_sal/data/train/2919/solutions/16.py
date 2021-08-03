def encode(message, key):
    key = str(key)
    return [ord(message[i]) - 96 + int(key[i % len(key)]) for i in range(0, len(message))]
