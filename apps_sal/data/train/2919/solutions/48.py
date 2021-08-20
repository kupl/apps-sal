import string
map = {ch: i + 1 for (i, ch) in enumerate(string.ascii_lowercase)}


def encode(message, key):
    key = str(key)
    res = []
    for (i, ch) in enumerate(message):
        res.append(map[ch] + int(key[i % len(key)]))
    return res
