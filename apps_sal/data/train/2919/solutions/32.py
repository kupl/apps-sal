def encode(message, key):
    # Code here
    al = "abcdefghijklmnopqrstuvwxyz"
    key = str(key)
    if len(message) > len(key): key = key*int(len(message)/len(key) + 1)
    out = []
    for i in list(message): out.append(al.index(i) + 1)
    for i in range(len(out)): out[i] = out[i] + int(key[i])
    return out
