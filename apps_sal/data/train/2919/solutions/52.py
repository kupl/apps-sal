def encode(message, key):
    return [i + int(l) for (i, l) in zip([' abcdefghijklmnopqrstuvwxyz'.index(i) for i in message], str(key) * (len(message) // len(str(key))) + str(key)[:len(message) % len(str(key))])]
