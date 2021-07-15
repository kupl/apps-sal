def encode(message, key):
    #horrible, but today felt like a one-liner kind of day
    return [ord(c) - 96 + int(str(key)[i%len(str(key))]) for i, c in enumerate(message)]

