def encode(message, key):
    return [ord(message[a]) - 96 + int(str(key)[a % len(str(key))]) for a in range(len(message))]
