def encode(message, key):
    ret = []
    d = dict()
    [d.update({chr(i): i - 96}) for i in range(97, 123)]
    for i in range(len(message)):
        ret.append(d[message[i]] + int(str(key)[i % len(str(key))]))
    return ret
