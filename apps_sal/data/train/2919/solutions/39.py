def encode(message, key):
    k = [int(x) for x in str(key)]
    l = len(k)

    return [n + k[i % l] for i, n in enumerate(ord(c) - 96 for c in message)]
