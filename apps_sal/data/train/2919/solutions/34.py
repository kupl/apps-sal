def encode(message, key):
    key = [int(k) for k in str(key)]
    l = len(key)
    return [ord(c) - 96 + key[i % l] for (i, c) in enumerate(message)]
