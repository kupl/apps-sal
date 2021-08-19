def encode(message, key):
    key = str(key) * len(message)
    return ['abcdefghijklmnopqrstuvwxyz'.index(m) + int(key[i]) + 1 for (i, m) in enumerate(message)]
