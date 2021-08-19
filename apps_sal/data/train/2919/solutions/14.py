def encode(message, key):
    key_digs = [int(dig) for dig in str(key)]
    result = [ord(ch) - 96 + key_digs[i % len(key_digs)] for (i, ch) in enumerate(message)]
    return result
