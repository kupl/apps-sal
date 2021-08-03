from string import ascii_lowercase as alpha


def encode(message, key):
    first = [alpha.index(x) + 1 for x in message]
    n, k = len(message), str(key)
    return [first[i] + int(k[i % len(k)]) for i in range(n)]
